<!DOCTYPE html>
<html>
<head>
    <title>AI Flood Control Admin</title>
    <link rel="stylesheet" href="/static/css/admin.css">
</head>
<body>

<header>
    <h1>⚙ AI Flood Intelligence Admin Control</h1>
    <a href="/" class="back-btn">⬅ Dashboard</a>
</header>

<div class="admin-grid">

    <!-- MODEL CONTROL -->
    <div class="admin-card">
        <h3>Model Control Center</h3>

        <button onclick="triggerTraining()">Train Models</button>
        <button onclick="triggerEvaluation()">Evaluate Models</button>
        <button onclick="restartEngine()">Restart Prediction Engine</button>

        <div class="threshold-control">
            <label>High Risk Threshold:</label>
            <input type="number" id="riskThreshold" value="0.7" step="0.05">
            <button onclick="updateThreshold()">Update</button>
        </div>

        <div>
            <label>
                <input type="checkbox" id="smsToggle" checked>
                SMS Alerts Enabled
            </label>
        </div>

        <div>
            <label>
                <input type="checkbox" id="emailToggle" checked>
                Email Alerts Enabled
            </label>
        </div>

    </div>

    <!-- SYSTEM STATUS -->
    <div class="admin-card">
        <h3>System Status</h3>

        <p>Database: <span id="dbStatus">Checking...</span></p>
        <p>MQTT Listener: <span id="mqttStatus">Checking...</span></p>
        <p>Prediction Engine: <span id="engineStatus">Checking...</span></p>

        <p>Random Forest Accuracy: <span id="rfAcc">--</span></p>
        <p>XGBoost Accuracy: <span id="xgbAcc">--</span></p>
        <p>LSTM Accuracy: <span id="lstmAcc">--</span></p>

    </div>

    <!-- LOG MONITOR -->
    <div class="admin-card full-width">
        <h3>Live System Logs</h3>
        <pre id="logs">Loading logs...</pre>
    </div>

    <!-- NAVIGATION -->
    <div class="admin-card">
        <h3>Analytics</h3>
        <a href="/admin/model-comparison">
            <button>Open Model Comparison</button>
        </a>
    </div>

</div>

<script>

const API_BASE = "/admin";

async function triggerTraining() {
    await fetch(`${API_BASE}/train`, {method:"POST"});
    alert("Model training started.");
}

async function triggerEvaluation() {
    await fetch(`${API_BASE}/evaluate`, {method:"POST"});
    alert("Model evaluation started.");
}

async function restartEngine() {
    await fetch(`${API_BASE}/restart`, {method:"POST"});
    alert("Prediction engine restarted.");
}

async function updateThreshold() {
    const value = document.getElementById("riskThreshold").value;
    await fetch(`${API_BASE}/threshold`, {
        method:"POST",
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({threshold:value})
    });
    alert("Threshold updated.");
}

async function fetchStatus() {

    const res = await fetch(`${API_BASE}/status`);
    const data = await res.json();

    document.getElementById("dbStatus").innerText = data.database;
    document.getElementById("mqttStatus").innerText = data.mqtt;
    document.getElementById("engineStatus").innerText = data.engine;

    document.getElementById("rfAcc").innerText = data.rf_accuracy;
    document.getElementById("xgbAcc").innerText = data.xgb_accuracy;
    document.getElementById("lstmAcc").innerText = data.lstm_accuracy;
}

async function fetchLogs() {
    const res = await fetch(`${API_BASE}/logs`);
    const data = await res.text();
    document.getElementById("logs").innerText = data;
}

setInterval(fetchStatus, 5000);
setInterval(fetchLogs, 5000);

fetchStatus();
fetchLogs();

</script>

</body>
</html>