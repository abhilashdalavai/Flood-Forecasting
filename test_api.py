<!DOCTYPE html>
<html>
<head>
    <title>Andhra Pradesh Flood Control Center</title>

    <link rel="stylesheet" href="/static/css/dashboard.css">
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css"/>

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <script src="https://unpkg.com/leaflet.heat/dist/leaflet-heat.js"></script>
</head>

<body>

<!-- ================= TOP BAR ================= -->

<div class="topbar">
    <div class="logo">
        🛰  Flood Intelligence Center
    </div>

    <div class="nav-buttons">
        <a href="/admin/" class="nav-btn">⚙ Admin Panel</a>
        <a href="/hydrodynamic-view" class="nav-btn">🌊 Hydrodynamic View</a>
    </div>

    <!-- Digital Clock + Mission Timer -->
    <div class="topbar-timers">
        <div class="clock-display">
            🕒 IST: <span id="liveClock">--:--:--</span>
        </div>
        <div class="mission-display">
            ⏱ Mission Time: <span id="missionTimer">00:00:00</span>
        </div>
    </div>
</div>

<!-- ================= ALERT ================= -->

<div id="alert-banner" class="alert-banner hidden">
    🚨 CRITICAL FLOOD RISK DETECTED 🚨
</div>

<!-- ================= MAIN LAYOUT ================= -->

<div class="main-container">

    <!-- ================= LEFT PANEL ================= -->
    <div class="left-panel">

        <!-- Prediction -->
        <div class="prediction-box">
            <h2>Live Flood Prediction</h2>

            <div id="risk-display" class="risk-box">
                <span id="risk_level">--</span>
            </div>

            <div class="confidence-container">
                <div class="progress-bar">
                    <div id="confidence-bar"></div>
                </div>
                <span id="confidence">0%</span>
            </div>
        </div>

        <!-- 3D Water Level -->
        <div class="water-level-container">
            <h3>🌊 River Water Level</h3>
            <div class="water-tank">
                <div id="waterFill" class="water-fill"></div>
                <div id="waterValue" class="water-value">0%</div>
            </div>
        </div>

        <!-- Weather Metrics -->
        <div class="weather-metrics">
            <div class="metric">Wind Speed: <span id="wind_speed">--</span></div>
            <div class="metric">Rainfall: <span id="rainfall">--</span></div>
            <div class="metric">River Flow: <span id="river_flow">--</span></div>
            <div class="metric">Temperature: <span id="temperature">--</span></div>
            <div class="metric">Humidity: <span id="humidity">--</span></div>
            <div class="metric">Pressure: <span id="pressure">--</span></div>
            <div class="metric">Flow Direction: <span id="flow_direction">--</span></div>
            <div class="metric">Hydrodynamic Index: <span id="hydrodynamic_index">--</span></div>
            <div class="metric snow">❄ Snow Fall: <span id="snow_fall">--</span></div>
            <div class="metric snow">🌊 Snow Melt: <span id="snow_melt">--</span></div>
        </div>

        <!-- Satellite Section -->
        <div class="satellite-box">
            <h3>🛰 Satellite Monitoring</h3>
            <div>Cloud Cover: <span id="cloud_cover">--</span></div>
            <div>Storm Activity: <span id="storm_activity">--</span></div>
            <div>Surface Moisture: <span id="surface_moisture">--</span></div>
        </div>

    </div>

    <!-- ================= RIGHT PANEL ================= -->
    <div class="right-panel">

        <!-- REALTIME TRENDS -->
        <div class="trend-grid">

            <div class="trend-card">
                <h3>Rainfall Trend</h3>
                <canvas id="rainfallChart"></canvas>
            </div>

            <div class="trend-card">
                <h3>River Flow Trend</h3>
                <canvas id="riverFlowChart"></canvas>
            </div>

            <div class="trend-card">
                <h3>Temperature Trend</h3>
                <canvas id="temperatureChart"></canvas>
            </div>

            <div class="trend-card">
                <h3>Humidity Trend</h3>
                <canvas id="humidityChart"></canvas>
            </div>

            <div class="trend-card">
                <h3>Snow Fall Trend</h3>
                <canvas id="snowFallChart"></canvas>
            </div>

            <div class="trend-card">
                <h3>Snow Melt Trend</h3>
                <canvas id="snowMeltChart"></canvas>
            </div>

        </div>

        <!-- Analytics Section -->
        <div class="analytics-section">

            <div class="chart-card">
                <h3>Probability Distribution</h3>
                <canvas id="probabilityChart"></canvas>
            </div>

            <div class="chart-card">
                <h3>Model Comparison</h3>
                <canvas id="modelComparisonChart"></canvas>
            </div>

        </div>

        <!-- Map Section -->
        <div class="map-card">
            <h3>🗺 Radar + Flood Heatmap Visualization</h3>
            <div id="map"></div>
        </div>

    </div>

</div>

<script src="/static/js/dashboard.js"></script>
</body>
</html>