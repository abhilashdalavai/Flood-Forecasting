<!DOCTYPE html>
<html>
<head>
    <title>Model Comparison</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="stylesheet" href="/static/css/admin.css">

    <style>
        .comparison-wrapper {
            max-width: 1100px;
            margin: 30px auto;
            padding: 20px;
        }

        .kpi-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }

        .kpi-card {
            background: #112240;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            border: 1px solid #00eaff33;
            box-shadow: 0 0 10px rgba(0,234,255,0.2);
        }

        .kpi-card h3 {
            margin: 0;
            font-size: 14px;
            color: #00eaff;
        }

        .kpi-card p {
            margin: 10px 0 0;
            font-size: 22px;
            font-weight: bold;
        }

        .charts-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
        }

        .chart-card {
            background: #112240;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #00eaff33;
        }

        .chart-card h3 {
            margin-top: 0;
            font-size: 14px;
            color: #00eaff;
        }

        canvas {
            max-height: 300px;
        }

        @media (max-width: 900px) {
            .charts-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>

<body>

<header>
    <h1>📊 AI Model Comparison</h1>
    <a href="/admin/panel">⬅ Back to Admin</a>
</header>

<div class="comparison-wrapper">

    <!-- KPI SUMMARY -->
    <div class="kpi-grid">
        <div class="kpi-card">
            <h3>Random Forest</h3>
            <p id="rfAcc">--</p>
        </div>
        <div class="kpi-card">
            <h3>XGBoost</h3>
            <p id="xgbAcc">--</p>
        </div>
        <div class="kpi-card">
            <h3>LSTM</h3>
            <p id="lstmAcc">--</p>
        </div>
    </div>

    <!-- CHARTS -->
    <div class="charts-grid">

        <div class="chart-card">
            <h3>Accuracy Comparison</h3>
            <canvas id="accuracyChart"></canvas>
        </div>

        <div class="chart-card">
            <h3>Prediction Probability Distribution</h3>
            <canvas id="probabilityChart"></canvas>
        </div>

    </div>

</div>

<script>

async function loadComparison() {

    const res = await fetch("/admin/model-metrics");
    const data = await res.json();

    // Update KPI numbers
    document.getElementById("rfAcc").innerText =
        (data.rf_accuracy * 100).toFixed(2) + "%";

    document.getElementById("xgbAcc").innerText =
        (data.xgb_accuracy * 100).toFixed(2) + "%";

    document.getElementById("lstmAcc").innerText =
        (data.lstm_accuracy * 100).toFixed(2) + "%";

    // Accuracy Chart
    new Chart(document.getElementById("accuracyChart"), {
        type: "bar",
        data: {
            labels: ["Random Forest", "XGBoost", "LSTM"],
            datasets: [{
                label: "Accuracy %",
                data: [
                    data.rf_accuracy * 100,
                    data.xgb_accuracy * 100,
                    data.lstm_accuracy * 100
                ],
                backgroundColor: ["#00eaff", "#9b59b6", "#1abc9c"]
            }]
        },
        options: {
            plugins: { legend: { display: false } },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100
                }
            }
        }
    });

    // Probability Chart
    new Chart(document.getElementById("probabilityChart"), {
        type: "doughnut",
        data: {
            labels: ["LOW", "MEDIUM", "HIGH"],
            datasets: [{
                data: [
                    data.sample_probs.LOW * 100,
                    data.sample_probs.MEDIUM * 100,
                    data.sample_probs.HIGH * 100
                ],
                backgroundColor: ["#2ecc71", "#f1c40f", "#e74c3c"]
            }]
        },
        options: {
            plugins: { legend: { position: "bottom" } }
        }
    });

}

loadComparison();

</script>

</body>
</html>