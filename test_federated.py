<!DOCTYPE html>
<html>
<head>
<title>Advanced Hydrodynamic Monitoring System</title>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/ol@v7.4.0/ol.css">
<script src="https://cdn.jsdelivr.net/npm/ol@v7.4.0/dist/ol.js"></script>

<style>
body { margin:0; font-family:Segoe UI; background:#0a192f; color:white; }

header {
    padding:15px;
    background:#071a2d;
    display:flex;
    justify-content:space-between;
    align-items:center;
}

header a {
    background:#00eaff;
    padding:6px 12px;
    color:black;
    border-radius:6px;
    text-decoration:none;
}

.layout {
    display:grid;
    grid-template-columns:2fr 1fr;
    gap:15px;
    padding:15px;
}

#map { height:650px; border-radius:10px; }

.panel { background:#112240; padding:15px; border-radius:10px; }

.timeline { margin-top:15px; }

input[type=range] { width:100%; }

button { padding:5px 10px; margin-top:8px; }
</style>
</head>

<body>

<header>
<h2>🌊 Hydrodynamic Monitoring System</h2>
<a href="/">Back</a>
</header>

<div class="layout">

<div id="map"></div>

<div class="panel">
<h3>Realtime Flood Severity</h3>
<div>Probability: <span id="probability">--</span></div>

<h3>AI Flood Direction</h3>
<div>Direction: <span id="aiDirection">--</span></div>

<h3>Playback Timeline</h3>
<div class="timeline">
<input type="range" id="timeSlider" min="0" max="10" value="0">
<button onclick="togglePlayback()">Play / Pause</button>
</div>

<h3>Layer Control</h3>
<button onclick="toggleLayer(districtLayer)">Locations</button>
<button onclick="toggleLayer(riverLayer)">Rivers</button>
<button onclick="toggleLayer(basinLayer)">Basins</button>
<button onclick="toggleLayer(radarLayer)">Radar</button>
</div>

</div>

<script>

const API_BASE = "/api";
let playbackInterval;
let isPlaying = false;

//////////////////////
// BASE MAP
//////////////////////

const map = new ol.Map({
target:'map',
layers:[
    new ol.layer.Tile({
        source:new ol.source.OSM()
    })
],
view:new ol.View({
    center:ol.proj.fromLonLat([80.6,16.5]),
    zoom:7
})
});

//////////////////////
// DISTRICT LAYER
//////////////////////

const districtLayer = new ol.layer.Vector({
source:new ol.source.Vector({
    url:`${API_BASE}/gis/districts.geojson`,
    format:new ol.format.GeoJSON()
})
});

map.addLayer(districtLayer);

function updateDistrictColor(intensity){

districtLayer.setStyle(function(){

let color='#2ecc71';
if(intensity>0.7) color='#e74c3c';
else if(intensity>0.4) color='#ffc107';

return new ol.style.Style({
fill:new ol.style.Fill({color:color}),
stroke:new ol.style.Stroke({color:'#ffffff',width:1})
});

});
}

//////////////////////
// RIVER NETWORK
//////////////////////

const riverLayer = new ol.layer.Vector({
source:new ol.source.Vector({
    url:`${API_BASE}/gis/rivers.geojson`,
    format:new ol.format.GeoJSON()
}),
style:new ol.style.Style({
    stroke:new ol.style.Stroke({
        color:'#00eaff',
        width:3
    })
})
});

map.addLayer(riverLayer);

//////////////////////
// BASIN LAYER
//////////////////////

const basinLayer = new ol.layer.Vector({
source:new ol.source.Vector({
    url:`${API_BASE}/gis/basins.geojson`,
    format:new ol.format.GeoJSON()
}),
style:new ol.style.Style({
    stroke:new ol.style.Stroke({color:'#ffc107',width:2}),
    fill:new ol.style.Fill({color:'rgba(255,193,7,0.1)'})
})
});

map.addLayer(basinLayer);

//////////////////////
// HEATMAP
//////////////////////

const heatLayer = new ol.layer.Heatmap({
source:new ol.source.Vector(),
radius:25,
blur:20
});
map.addLayer(heatLayer);

//////////////////////
// RADAR LAYER
//////////////////////

const radarLayer = new ol.layer.Tile({
source:new ol.source.XYZ({
    url:'https://tile.openweathermap.org/map/precipitation_new/{z}/{x}/{y}.png?appid=YOUR_API_KEY'
}),
opacity:0.5
});
map.addLayer(radarLayer);

//////////////////////
// AI FLOOD PATH ROUTING
//////////////////////

let pathLayer;

function animateFloodPath(prob){

if(pathLayer) map.removeLayer(pathLayer);

const direction = prob>0.6 ? [81.5,17.5] : [79.8,15.5];

document.getElementById("aiDirection").innerText =
prob>0.6 ? "North-East" : "South-West";

const line = new ol.geom.LineString([
ol.proj.fromLonLat([80.6,16.5]),
ol.proj.fromLonLat(direction)
]);

pathLayer = new ol.layer.Vector({
source:new ol.source.Vector({
    features:[new ol.Feature(line)]
}),
style:new ol.style.Style({
    stroke:new ol.style.Stroke({
        color:'#ff4b2b',
        width:4
    })
})
});

map.addLayer(pathLayer);
}

//////////////////////
// FLOOD SPREAD
//////////////////////

let floodLayer;

function updateFloodSpread(prob){

if(floodLayer) map.removeLayer(floodLayer);

const radius = prob*60000;

const circle = new ol.geom.Circle(
ol.proj.fromLonLat([80.6,16.5]),
radius
);

floodLayer = new ol.layer.Vector({
source:new ol.source.Vector({
features:[new ol.Feature(circle)]
}),
style:new ol.style.Style({
fill:new ol.style.Fill({
color:'rgba(255,0,0,0.25)'
})
})
});

map.addLayer(floodLayer);
}

//////////////////////
// HEATMAP UPDATE
//////////////////////

function updateHeatmap(prob){

const point = new ol.Feature({
geometry:new ol.geom.Point(
ol.proj.fromLonLat([80.6,16.5])
)
});

heatLayer.getSource().clear();
heatLayer.getSource().addFeature(point);
}

//////////////////////
// REALTIME DATA
//////////////////////

async function fetchPrediction(){

const res = await fetch(`${API_BASE}/predict`);
const data = await res.json();

const high = data.probabilities.HIGH;

document.getElementById("probability").innerText =
(high*100).toFixed(1)+"%";

updateFloodSpread(high);
updateHeatmap(high);
updateDistrictColor(high);
animateFloodPath(high);
}

//////////////////////
// PLAYBACK
//////////////////////

function togglePlayback(){

if(isPlaying){
clearInterval(playbackInterval);
isPlaying=false;
}else{
playbackInterval=setInterval(()=>{
let slider=document.getElementById("timeSlider");
slider.value=parseInt(slider.value)+1;
if(slider.value>10) slider.value=0;
simulateHistorical(parseInt(slider.value));
},1000);
isPlaying=true;
}
}

function simulateHistorical(step){
const fakeProb=step/10;
updateFloodSpread(fakeProb);
updateHeatmap(fakeProb);
updateDistrictColor(fakeProb);
animateFloodPath(fakeProb);
}

//////////////////////
// LAYER TOGGLE
//////////////////////

function toggleLayer(layer){
layer.setVisible(!layer.getVisible());
}

//////////////////////

setInterval(fetchPrediction,4000);
fetchPrediction();

</script>

</body>
</html>