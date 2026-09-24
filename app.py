import streamlit as st
import csv
from pathlib import Path
from statistics import mean
import math

# ============================================================
# PAGE SETUP
# ============================================================

st.set_page_config(
    page_title="ShambaPulse AI",
    page_icon="🌱",
    layout="wide"
)

# ============================================================
# UI STYLE
# ============================================================

st.markdown("""
<style>
    .main-title {
        font-size: 2.4rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        color: #5f6b66;
        font-size: 1.05rem;
        margin-bottom: 0.2rem;
    }

    .section-note {
        color: #6b7280;
        font-size: 0.9rem;
    }

    .insight-card {
        padding: 1rem 1.2rem;
        border-radius: 12px;
        border: 1px solid rgba(128,128,128,0.25);
        background: rgba(128,128,128,0.06);
        margin: 0.5rem 0 1rem 0;
    }

    .flow-card {
        text-align: center;
        padding: 0.8rem 0.4rem;
        border-radius: 10px;
        border: 1px solid rgba(128,128,128,0.22);
        background: rgba(128,128,128,0.04);
    }

    .small-muted {
        color: #6b7280;
        font-size: 0.82rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🌱 ShambaPulse AI")

    st.caption("Environmental Risk Intelligence")

    st.divider()

    st.markdown("### 📡 Data Source")
    st.write("Conduit@Empathy")

    st.markdown("### 🌍 Monitoring Site")
    st.write("Site JKUAT")
    st.write("Kiambu, Kenya")

    st.markdown("### 📊 Dataset")
    st.write("7,062 environmental measurements")

    st.divider()

    st.markdown("### 🛡️ System")

    st.success("Data Connected")
    st.success("Analysis Active")
    st.success("Fail-Safe Active")

    st.divider()

    st.caption(
        "ShambaPulse AI converts environmental "
        "data into explainable monitoring intelligence."
    )

# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🌱 ShambaPulse AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Environmental Risk Intelligence for Resilient Farming</div>',
    unsafe_allow_html=True
)

st.write(
    "From real environmental data to explainable monitoring decisions."
)

st.caption(
    "Powered by real Conduit@Empathy sensor observations"
)

# ============================================================
# CURRENT FARM SITUATION PLACEHOLDER
# ============================================================

farm_situation_placeholder = st.empty()

# ============================================================
# LOAD CONDUIT CSV
# ============================================================

DATA_FILE = Path("conduit_data.csv")

if not DATA_FILE.exists():

    st.error(
        "conduit_data.csv not found. "
        "Please keep it in the same folder as app.py."
    )

    st.stop()

rows = []

with open(DATA_FILE, "r", encoding="utf-8-sig") as file:

    data_lines = (
        line
        for line in file
        if not line.startswith("#")
    )

    reader = csv.DictReader(data_lines)

    for row in reader:
        rows.append(row)

if not rows:

    st.error(
        "No measurement rows found in conduit_data.csv."
    )

    st.stop()

st.success(
    f"Conduit dataset loaded successfully — {len(rows):,} measurements"
)

# ============================================================
# CONVERT SELECTED VALUES
# ============================================================

temperatures = [
    float(r["SHT Temperature"])
    for r in rows
    if r["SHT Temperature"].strip()
]

humidity = [
    float(r["SHT Humidity"])
    for r in rows
    if r["SHT Humidity"].strip()
]

wind_speed = [
    float(r["Wind Speed"])
    for r in rows
    if r["Wind Speed"].strip()
]

rainfall = [
    float(r["Rain Gauge 1"])
    for r in rows
    if r["Rain Gauge 1"].strip()
]

heat_index = [
    float(r["Heat Index"])
    for r in rows
    if r["Heat Index"].strip()
]

wet_bulb = [
    float(r["Wet Bulb Temperature"])
    for r in rows
    if r["Wet Bulb Temperature"].strip()
]

# ============================================================
# CURRENT ENVIRONMENTAL CONDITIONS
# ============================================================

st.markdown("### 📊 Current Environmental Conditions")

latest = rows[-1]

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Temperature",
    f"{float(latest['SHT Temperature']):.1f} °C"
)

col2.metric(
    "Humidity",
    f"{float(latest['SHT Humidity']):.1f} %"
)

col3.metric(
    "Rain Gauge",
    f"{float(latest['Rain Gauge 1']):.1f} mm"
)

col4.metric(
    "Wind Speed",
    f"{float(latest['Wind Speed']):.1f} m/s"
)

col5.metric(
    "Heat Index",
    f"{float(latest['Heat Index']):.1f} °C"
)

# ============================================================
# DATASET SUMMARY
# ============================================================

st.markdown("### 🔎 Dataset Summary")

summary_col1, summary_col2, summary_col3 = st.columns(3)

overall_avg_temp = mean(temperatures)
overall_avg_humidity = mean(humidity)
overall_avg_wind = mean(wind_speed)

summary_col1.metric(
    "Average Temperature",
    f"{overall_avg_temp:.1f} °C"
)

summary_col2.metric(
    "Average Humidity",
    f"{overall_avg_humidity:.1f} %"
)

summary_col3.metric(
    "Average Wind Speed",
    f"{overall_avg_wind:.1f} m/s"
)

# ============================================================
# RECENT CONDUIT OBSERVATIONS
# ============================================================

st.markdown("### 🕒 Recent Conduit Observations")

display_columns = [
    "Time",
    "Rain Gauge 1",
    "SHT Temperature",
    "SHT Humidity",
    "Wind Speed",
    "Heat Index",
    "Wet Bulb Globe Temperature"
]

st.dataframe(
    [
        {
            column: row[column]
            for column in display_columns
        }
        for row in rows[-20:]
    ],
    use_container_width=True
)

# ============================================================
# ENVIRONMENTAL SIGNAL
# ============================================================

st.markdown("### ⚠️ Environmental Signal")

current_temp = float(latest["SHT Temperature"])
current_humidity = float(latest["SHT Humidity"])
current_wind = float(latest["Wind Speed"])

temp_deviation = current_temp - overall_avg_temp
humidity_deviation = current_humidity - overall_avg_humidity

if (
    current_temp > overall_avg_temp
    and current_humidity < overall_avg_humidity
):

    st.warning(
        "Changing environmental conditions detected: "
        "temperature is above the dataset average while "
        "humidity is below average."
    )

else:

    st.info(
        "Current conditions are within the basic historical range "
        "of the loaded Conduit observations."
    )

st.caption(
    "This prototype currently provides environmental indicators, "
    "not a crop-yield or crop-failure prediction."
)

# ============================================================
# ENVIRONMENTAL TRENDS
# ============================================================

st.markdown("## 📈 Environmental Trends")

recent_rows = rows[-200:]

trend_temperature = []
trend_humidity = []
trend_rainfall = []

for r in recent_rows:

    try:
        temp = float(r["SHT Temperature"])

        if -50 <= temp <= 60:
            trend_temperature.append(temp)

    except (ValueError, TypeError):
        pass

    try:
        hum = float(r["SHT Humidity"])

        if 0 <= hum <= 100:
            trend_humidity.append(hum)

    except (ValueError, TypeError):
        pass

    try:
        rain = float(r["Rain Gauge 1"])

        if rain >= 0:
            trend_rainfall.append(rain)

    except (ValueError, TypeError):
        pass

st.markdown("### 🌡️ Temperature Trend")

if trend_temperature:
    st.line_chart(
        {"Temperature (°C)": trend_temperature},
        height=300
    )
else:
    st.warning("No valid temperature observations available.")

st.markdown("### 💧 Humidity Trend")

if trend_humidity:
    st.line_chart(
        {"Humidity (%)": trend_humidity},
        height=300
    )
else:
    st.warning("No valid humidity observations available.")

st.markdown("### 🌧️ Rainfall Trend")

if trend_rainfall:
    st.line_chart(
        {"Rainfall (mm)": trend_rainfall},
        height=300
    )
else:
    st.warning("No valid rainfall observations available.")

st.caption(
    "Charts show validated recent environmental observations "
    "from the Conduit@Empathy dataset."
)

# ============================================================
# ENVIRONMENTAL ANOMALY DETECTION
# ============================================================

st.markdown("## 🔍 Environmental Anomaly Detection")

baseline_rows = rows[-120:-20]
recent_anomaly_rows = rows[-20:]

baseline_temperature = [
    float(r["SHT Temperature"])
    for r in baseline_rows
    if r["SHT Temperature"].strip()
]

baseline_humidity = [
    float(r["SHT Humidity"])
    for r in baseline_rows
    if r["SHT Humidity"].strip()
]

baseline_wind = [
    float(r["Wind Speed"])
    for r in baseline_rows
    if r["Wind Speed"].strip()
]

baseline_rainfall = [
    float(r["Rain Gauge 1"])
    for r in baseline_rows
    if r["Rain Gauge 1"].strip()
]

recent_temperature = [
    float(r["SHT Temperature"])
    for r in recent_anomaly_rows
    if r["SHT Temperature"].strip()
]

recent_humidity = [
    float(r["SHT Humidity"])
    for r in recent_anomaly_rows
    if r["SHT Humidity"].strip()
]

recent_wind = [
    float(r["Wind Speed"])
    for r in recent_anomaly_rows
    if r["Wind Speed"].strip()
]

recent_rainfall = [
    float(r["Rain Gauge 1"])
    for r in recent_anomaly_rows
    if r["Rain Gauge 1"].strip()
]

baseline_temp_avg = mean(baseline_temperature)
baseline_humidity_avg = mean(baseline_humidity)
baseline_wind_avg = mean(baseline_wind)

recent_temp_avg = mean(recent_temperature)
recent_humidity_avg = mean(recent_humidity)
recent_wind_avg = mean(recent_wind)

temperature_change = recent_temp_avg - baseline_temp_avg
humidity_change = recent_humidity_avg - baseline_humidity_avg
wind_change = recent_wind_avg - baseline_wind_avg

recent_rain_total = sum(recent_rainfall)
baseline_rain_total = sum(baseline_rainfall)

rainfall_change = (
    mean(recent_rainfall)
    - mean(baseline_rainfall)
)

anomaly_col1, anomaly_col2, anomaly_col3, anomaly_col4 = st.columns(4)

anomaly_col1.metric(
    "Temperature Change",
    f"{temperature_change:+.2f} °C"
)

anomaly_col2.metric(
    "Humidity Change",
    f"{humidity_change:+.2f} %"
)

anomaly_col3.metric(
    "Wind Change",
    f"{wind_change:+.2f} m/s"
)

anomaly_col4.metric(
    "Rainfall Change",
    f"{rainfall_change:+.2f} mm"
)

TEMP_SHIFT = 2.0
HUMIDITY_SHIFT = 10.0
WIND_SHIFT = 1.0

anomaly_reasons = []
anomaly_score = 0

if abs(temperature_change) >= TEMP_SHIFT:

    anomaly_score += 1

    direction = "increased" if temperature_change > 0 else "decreased"

    anomaly_reasons.append(
        f"Recent temperature {direction} by "
        f"{abs(temperature_change):.2f} °C compared with "
        "the previous baseline."
    )

if abs(humidity_change) >= HUMIDITY_SHIFT:

    anomaly_score += 1

    direction = "increased" if humidity_change > 0 else "decreased"

    anomaly_reasons.append(
        f"Recent humidity {direction} by "
        f"{abs(humidity_change):.2f}% compared with "
        "the previous baseline."
    )

if abs(wind_change) >= WIND_SHIFT:

    anomaly_score += 1

    direction = "increased" if wind_change > 0 else "decreased"

    anomaly_reasons.append(
        f"Recent wind speed {direction} by "
        f"{abs(wind_change):.2f} m/s compared with "
        "the previous baseline."
    )

if baseline_rain_total == 0 and recent_rain_total > 0:

    anomaly_score += 1

    anomaly_reasons.append(
        "Rainfall was observed in the recent window "
        "after no rainfall was observed in the previous baseline window."
    )

elif baseline_rain_total > 0:

    rainfall_ratio = recent_rain_total / baseline_rain_total

    if rainfall_ratio >= 2 or rainfall_ratio <= 0.5:

        anomaly_score += 1

        anomaly_reasons.append(
            "Recent rainfall accumulation differs substantially "
            "from the previous observation window."
        )

if anomaly_score >= 3:

    anomaly_status = "🔴 ATTENTION"

    anomaly_message = (
        "Multiple environmental signals show a meaningful "
        "shift from the recent baseline."
    )

elif anomaly_score >= 1:

    anomaly_status = "🟡 WATCH"

    anomaly_message = (
        "A meaningful environmental shift was detected "
        "in at least one monitored signal."
    )

else:

    anomaly_status = "🟢 STABLE"

    anomaly_message = (
        "No meaningful environmental shift was detected "
        "in the monitored signals."
    )

st.metric(
    "Environmental Anomaly Status",
    anomaly_status
)

st.write(anomaly_message)

if anomaly_reasons:

    st.markdown("### 🔎 Why was this detected?")

    for reason in anomaly_reasons:
        st.write("•", reason)

else:

    st.write(
        "• Temperature, humidity, wind and rainfall remain "
        "within the prototype's monitored shift ranges."
    )

st.caption(
    "The anomaly engine compares recent Conduit observations "
    "with an earlier observation window. The thresholds are "
    "prototype monitoring rules, not scientifically validated "
    "crop-risk thresholds."
)

# ============================================================
# FAIL-SAFE
# ============================================================

st.markdown("### 🛡️ Data Confidence & Fail-Safe")

required_fields = [
    "SHT Temperature",
    "SHT Humidity",
    "Wind Speed",
    "Rain Gauge 1"
]

missing_fields = []

for field in required_fields:

    if not latest[field].strip():
        missing_fields.append(field)

if missing_fields:

    st.warning(
        "⚠️ Some required sensor values are unavailable. "
        "ShambaPulse will avoid strong environmental conclusions."
    )

else:

    st.success(
        "✅ Required monitored sensor values are available. "
        "Environmental analysis can continue."
    )

st.caption(
    "The fail-safe layer avoids presenting a strong conclusion "
    "when required sensor inputs are unavailable."
)

# ============================================================
# RISK MONITOR
# ============================================================

st.markdown("## 🛡️ ShambaPulse Risk Monitor")

avg_temp = overall_avg_temp
avg_humidity = overall_avg_humidity
avg_wind = overall_avg_wind

risk_points = 0
reasons = []

if temp_deviation > 2:

    risk_points += 1

    reasons.append(
        "Temperature is noticeably above the dataset baseline."
    )

if humidity_deviation < -10:

    risk_points += 1

    reasons.append(
        "Humidity is noticeably below the dataset baseline."
    )

if current_wind > avg_wind * 2:

    risk_points += 1

    reasons.append(
        "Wind speed is considerably above the dataset baseline."
    )

if anomaly_score >= 3:

    risk_points += 1

    reasons.append(
        "Multiple recent environmental signals "
        "show a meaningful shift."
    )

if risk_points == 0:

    risk_level = "🟢 NORMAL"

    risk_message = (
        "Current conditions are close to the observed baseline."
    )

elif risk_points == 1:

    risk_level = "🟡 WATCH"

    risk_message = (
        "One environmental indicator requires continued monitoring."
    )

else:

    risk_level = "🔴 HIGH ATTENTION"

    risk_message = (
        "Multiple environmental indicators require closer monitoring."
    )

st.metric(
    "Environmental Risk",
    risk_level
)

st.write(risk_message)

if reasons:

    st.markdown("### 🔎 Why?")

    for reason in reasons:
        st.write("•", reason)

else:

    st.write(
        "• No major deviation detected in the monitored indicators."
    )

# ============================================================
# DECISION SUPPORT
# ============================================================

st.markdown("### 📌 Decision Support")

if risk_points >= 2:

    st.warning(
        "Monitor the farm environment more closely "
        "and verify new sensor readings before taking "
        "environment-sensitive action."
    )

elif risk_points == 1:

    st.info(
        "Continue monitoring environmental conditions "
        "for further changes."
    )

else:

    st.success(
        "Continue normal environmental monitoring. "
        "No major deviation detected."
    )

st.caption(
    "ShambaPulse provides environmental monitoring and "
    "decision support. It does not predict crop failure "
    "or replace agricultural expertise."
)

# ============================================================
# ENVIRONMENTAL PATTERN INTELLIGENCE
# ============================================================

st.markdown("## 🤖 Environmental Pattern Intelligence")

st.write(
    "ShambaPulse uses a lightweight unsupervised statistical "
    "detector to compare the latest environmental pattern "
    "with patterns observed in the Conduit dataset."
)

feature_names = [
    "Temperature",
    "Humidity",
    "Wind Speed",
    "Heat Index",
    "Wet Bulb Temperature"
]

feature_rows = []

for row in rows:

    try:

        feature_rows.append([
            float(row["SHT Temperature"]),
            float(row["SHT Humidity"]),
            float(row["Wind Speed"]),
            float(row["Heat Index"]),
            float(row["Wet Bulb Temperature"])
        ])

    except (ValueError, TypeError):
        continue

pattern_status = "🟢 NORMAL"
latest_pattern_score = 0.0
pattern_message = (
    "Environmental pattern analysis is not available."
)

displayed_contributions_list = []

if len(feature_rows) < 100:

    st.warning(
        "Not enough valid observations for environmental "
        "pattern analysis."
    )

else:

    reference = feature_rows[:-20]
    latest_features = feature_rows[-20:]

    feature_means = []

    for column_index in range(5):

        column_values = [
            row[column_index]
            for row in reference
        ]

        feature_means.append(
            mean(column_values)
        )

    feature_stds = []

    for column_index in range(5):

        column_values = [
            row[column_index]
            for row in reference
        ]

        column_mean = mean(column_values)

        variance = mean([
            (value - column_mean) ** 2
            for value in column_values
        ])

        standard_deviation = math.sqrt(variance)

        if standard_deviation == 0:
            standard_deviation = 0.0001

        feature_stds.append(standard_deviation)

    recent_distances = []

    for observation in latest_features:

        squared_z_values = []

        for index in range(5):

            z_value = (
                observation[index]
                - feature_means[index]
            ) / feature_stds[index]

            squared_z_values.append(z_value ** 2)

        distance = math.sqrt(
            mean(squared_z_values)
        )

        recent_distances.append(distance)

    latest_pattern_score = mean(recent_distances)

    if latest_pattern_score < 1.0:

        pattern_status = "🟢 NORMAL"

        pattern_message = (
            "The latest environmental pattern is close "
            "to patterns observed in the historical data."
        )

    elif latest_pattern_score < 2.0:

        pattern_status = "🟡 UNUSUAL"

        pattern_message = (
            "The latest environmental pattern differs "
            "moderately from the historical pattern."
        )

    else:

        pattern_status = "🔴 HIGH VARIATION"

        pattern_message = (
            "The latest environmental pattern differs "
            "substantially from the historical pattern."
        )

    ml_col1, ml_col2 = st.columns(2)

    ml_col1.metric(
        "Environmental Pattern",
        pattern_status
    )

    ml_col2.metric(
        "Pattern Distance",
        f"{latest_pattern_score:.2f}"
    )

    st.write(pattern_message)

    st.markdown("### 🔎 Pattern Explanation")

    latest_average = []

    for index in range(5):

        latest_average.append(
            mean([
                observation[index]
                for observation in latest_features
            ])
        )

    contributions = []

    for index in range(5):

        z_value = (
            latest_average[index]
            - feature_means[index]
        ) / feature_stds[index]

        contributions.append(
            (
                feature_names[index],
                abs(z_value),
                z_value
            )
        )

    contributions.sort(
        key=lambda item: item[1],
        reverse=True
    )

    for name, magnitude, signed_value in contributions:

        if magnitude >= 1.0:

            direction = (
                "above"
                if signed_value > 0
                else "below"
            )

            displayed_contributions_list.append(
                f"{name} is {direction} its historical pattern."
            )

            st.write(
                f"• **{name}** is {direction} its "
                f"historical pattern."
            )

    if not displayed_contributions_list:

        st.write(
            "• No individual environmental feature shows "
            "a large deviation from its historical pattern."
        )

    st.caption(
        "This is an unsupervised statistical pattern detector, "
        "not a crop-failure prediction model. Its score measures "
        "distance from the observed environmental baseline."
    )

# ============================================================
# DATA → INTELLIGENCE → ACTION
# ============================================================

st.markdown("## 🔄 ShambaPulse Intelligence Flow")

flow1, flow2, flow3, flow4 = st.columns(4)

with flow1:
    st.markdown(
        '<div class="flow-card"><b>📡 DATA</b><br>'
        '<span class="small-muted">Conduit@Empathy observations</span></div>',
        unsafe_allow_html=True
    )

with flow2:
    st.markdown(
        '<div class="flow-card"><b>🔍 ANALYZE</b><br>'
        '<span class="small-muted">Trends + anomalies + patterns</span></div>',
        unsafe_allow_html=True
    )

with flow3:
    st.markdown(
        '<div class="flow-card"><b>🛡️ VERIFY</b><br>'
        '<span class="small-muted">Fail-safe + uncertainty checks</span></div>',
        unsafe_allow_html=True
    )

with flow4:
    st.markdown(
        '<div class="flow-card"><b>🌾 ACT</b><br>'
        '<span class="small-muted">Farmer-friendly monitoring guidance</span></div>',
        unsafe_allow_html=True
    )

# ============================================================
# SYSTEM STATUS
# ============================================================

st.markdown("## 🧭 ShambaPulse System Status")

st.success(
    "✅ Conduit data → environmental analysis → "
    "anomaly detection → fail-safe → decision support → "
    "pattern intelligence"
)

st.caption(
    "ShambaPulse is designed as an environmental monitoring "
    "and decision-support prototype for resilient farming."
)

# ============================================================
# FARMER ACTION INTELLIGENCE
# ============================================================

st.markdown("## 🌾 Farmer Action Intelligence")

st.write(
    "ShambaPulse converts environmental signals into "
    "simple monitoring guidance without making unsupported "
    "crop-failure or treatment claims."
)

action_reasons = []

if anomaly_score >= 3:

    action_reasons.append(
        "Multiple environmental signals changed from the recent baseline."
    )

elif anomaly_score >= 1:

    action_reasons.append(
        "At least one environmental signal changed from the recent baseline."
    )

if pattern_status == "🟡 UNUSUAL":

    action_reasons.append(
        "The latest combination of environmental variables differs "
        "moderately from the historical pattern."
    )

elif pattern_status == "🔴 HIGH VARIATION":

    action_reasons.append(
        "The latest combination of environmental variables differs "
        "substantially from the historical pattern."
    )

if risk_points >= 2:

    action_reasons.append(
        "Multiple monitored indicators require closer observation."
    )

elif risk_points == 1:

    action_reasons.append(
        "One monitored environmental indicator requires continued observation."
    )

if (
    pattern_status == "🔴 HIGH VARIATION"
    or risk_points >= 2
    or anomaly_score >= 3
):

    action_status = "🔴 INCREASE MONITORING"

    action_message = (
        "Several environmental signals require closer monitoring. "
        "Verify upcoming sensor observations before making "
        "environment-sensitive decisions."
    )

    action_steps = [
        "Check the next available sensor observations.",
        "Verify that unusual readings are consistent rather than isolated.",
        "Avoid making decisions based on a single unusual measurement.",
        "Use local agricultural knowledge before taking crop-specific action."
    ]

elif (
    pattern_status == "🟡 UNUSUAL"
    or risk_points == 1
    or anomaly_score >= 1
):

    action_status = "🟡 WATCH"

    action_message = (
        "An environmental change has been detected. "
        "Continue monitoring and verify whether the pattern persists."
    )

    action_steps = [
        "Continue observing the environmental indicators.",
        "Check upcoming sensor readings for persistence.",
        "Compare new observations with the recent baseline.",
        "Seek crop-specific guidance before taking major action."
    ]

else:

    action_status = "🟢 ROUTINE MONITORING"

    action_message = (
        "Current environmental conditions are close to the "
        "observed baseline. Continue routine monitoring."
    )

    action_steps = [
        "Continue routine environmental monitoring.",
        "Watch for changes in temperature, humidity, wind and rainfall.",
        "Verify unusual future readings before acting on them."
    ]

action_col1, action_col2 = st.columns(2)

action_col1.metric(
    "Recommended Monitoring Level",
    action_status
)

action_col2.metric(
    "Signals Requiring Attention",
    len(action_reasons)
)

st.write(action_message)

if action_reasons:

    st.markdown(
        "### 🔎 Why is ShambaPulse recommending this?"
    )

    for reason in action_reasons:
        st.write("•", reason)

st.markdown("### 📌 Suggested Monitoring Actions")

for step in action_steps:
    st.write("→", step)

st.info(
    "🛡️ ShambaPulse provides environmental monitoring guidance. "
    "It does not replace local agricultural expertise and does "
    "not provide crop-specific treatment instructions."
)

st.caption(
    "Action recommendations are generated from observed "
    "environmental patterns, anomaly signals and system "
    "risk indicators."
)

# ============================================================
# WHY IS SHAMBAPULSE WATCHING?
# ============================================================

st.markdown("## 🧠 Why is ShambaPulse Watching?")

explanation_col1, explanation_col2 = st.columns(2)

with explanation_col1:

    st.markdown("### 📊 Current vs Historical")

    current_vs_rows = [
        ["Temperature", f"{current_temp:.1f} °C", f"{overall_avg_temp:.1f} °C"],
        ["Humidity", f"{current_humidity:.1f} %", f"{overall_avg_humidity:.1f} %"],
        ["Wind Speed", f"{current_wind:.1f} m/s", f"{overall_avg_wind:.1f} m/s"],
    ]

    st.dataframe(
        current_vs_rows,
        column_config={
            0: "Indicator",
            1: "Current",
            2: "Dataset Average"
        },
        hide_index=True,
        use_container_width=True
    )

with explanation_col2:

    st.markdown("### 🔎 Intelligence Signals")

    st.write(
        f"• **Monitoring level:** {action_status}"
    )

    st.write(
        f"• **Environmental risk:** {risk_level}"
    )

    st.write(
        f"• **Pattern status:** {pattern_status}"
    )

    st.write(
        f"• **Pattern distance:** {latest_pattern_score:.2f}"
    )

    st.write(
        f"• **Recent anomaly score:** {anomaly_score}"
    )

st.markdown(
    '<div class="insight-card">'
    '<b>💡 What this means</b><br>'
    'ShambaPulse does not assume that one unusual reading means a crop problem. '
    'It combines recent environmental changes, historical comparison and '
    'multi-variable pattern variation before increasing the monitoring level.'
    '</div>',
    unsafe_allow_html=True
)

st.caption(
    "The system is designed to detect environmental change and support "
    "verification. It does not diagnose crop disease, predict crop failure "
    "or prescribe crop-specific treatment."
)


# ============================================================
# CURRENT FARM SITUATION
# ============================================================

with farm_situation_placeholder.container(border=True):

    st.markdown("### 🌾 Current Farm Situation")

    situation_col1, situation_col2, situation_col3 = st.columns(3)

    situation_col1.metric(
        "Monitoring Status",
        action_status
    )

    situation_col2.metric(
        "Environmental Risk",
        risk_level
    )

    situation_col3.metric(
        "Environmental Pattern",
        pattern_status
    )

    st.write(action_message)

    if action_reasons:

        st.markdown("#### 🔎 Why?")

        for reason in action_reasons[:2]:
            st.write("•", reason)

    st.markdown("#### 📌 Recommended")

    st.write(
        f"→ {action_steps[0]}"
    )

    st.caption(
        "This panel summarizes the current environmental "
        "monitoring state from Conduit@Empathy observations."
    )
