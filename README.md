# 🌱 ShambaPulse AI

### Environmental Risk Intelligence for Resilient Farming

ShambaPulse AI is an environmental monitoring and early-warning prototype that transforms real-world environmental sensor observations into understandable monitoring insights for resilient farming.

Instead of simply displaying weather measurements, ShambaPulse AI analyzes recent environmental conditions against historical observations, detects unusual changes, verifies data reliability, and provides farmer-friendly monitoring guidance.

---

## 🌍 Problem

Farmers are increasingly exposed to changing environmental conditions such as temperature variation, humidity changes, rainfall variability, and unusual combinations of environmental factors.

Raw sensor data can show what is happening, but it does not always explain whether current conditions are normal or changing in an unusual way.

ShambaPulse AI addresses this gap by converting environmental observations into simple, explainable monitoring signals.

---

## 💡 Solution

ShambaPulse AI follows a simple intelligence pipeline:

**Data → Analyze → Verify → Act**

1. **Data** — Collect real environmental observations from Conduit@Empathy.
2. **Analyze** — Examine trends, recent changes, anomalies, and multi-variable environmental patterns.
3. **Verify** — Apply data availability checks and fail-safe logic before generating guidance.
4. **Act** — Convert the analysis into understandable monitoring guidance.

---

## 🌦️ Conduit@Empathy Data

The prototype uses real environmental observations from **Conduit@Empathy**.

The dataset contains measurements including:

- Temperature
- Humidity
- Rainfall
- Wind Speed
- Wind Gust
- Heat Index
- Wet Bulb Temperature
- Wet Bulb Globe Temperature
- Wind Direction
- Atmospheric Pressure

### Dataset Information

- **Monitoring Site:** Site JKUAT / Kiambu, Kenya
- **Measurements:** 7,062 environmental observations
- **Instrument:** Kenya Kiambu JKUAT IoT AWS - Conduti@Empathy1
- **Data Source:** 3D-FEWSNET
- **DOI:** https://doi.org/10.5065/d6v1236q

The Conduit data is used directly in the application's analysis and decision-support pipeline rather than being displayed only as raw information.

---

## 🧠 Intelligence Features

### 1. Environmental Monitoring

The dashboard displays current environmental conditions such as:

- Temperature
- Humidity
- Rainfall
- Wind Speed
- Heat Index

---

### 2. Environmental Trends

Recent observations are visualized to help identify changes in environmental conditions over time.

The dashboard provides trend information for important environmental indicators, helping users understand how conditions have been changing.

---

### 3. Anomaly Detection

ShambaPulse compares recent observations with a historical baseline to identify noticeable changes in:

- Temperature
- Humidity
- Wind
- Rainfall

The current implementation uses transparent prototype monitoring rules rather than claiming scientifically validated crop-risk thresholds.

---

### 4. Environmental Pattern Intelligence

The system compares the recent multi-variable environmental pattern with historical observations.

The pattern detector uses:

- Temperature
- Humidity
- Wind Speed
- Heat Index
- Wet Bulb Temperature

The detector is an **unsupervised statistical pattern detector**.

It does **not** claim to be a trained crop-failure prediction model.

---

### 5. Fail-Safe Layer

The system is designed to avoid producing misleading conclusions when environmental data is unreliable or unavailable.

The fail-safe layer checks whether required monitored values are available before continuing analysis.

Instead of generating a potentially misleading prediction, the system can communicate that monitoring is limited when required data is unavailable.

---

### 6. Farmer Action Intelligence

Technical analysis is converted into simple monitoring guidance.

Example:

> An environmental change has been detected. Continue monitoring and verify whether the pattern persists.

The system focuses on monitoring guidance rather than diagnosing crop diseases or prescribing agricultural treatments.

---

## 🔄 Intelligence Flow

```text
Conduit@Empathy
      ↓
Environmental Observations
      ↓
Data Validation
      ↓
Trend Analysis
      ↓
Anomaly Detection
      ↓
Pattern Intelligence
      ↓
Fail-Safe Verification
      ↓
Risk & Monitoring Status
      ↓
Farmer Action Intelligence
```

---
## 🤖 AI / Analytics Usage

ShambaPulse AI uses an unsupervised statistical pattern detector to compare recent multi-variable environmental conditions with historical observations.

The analysis considers environmental signals such as:

- Temperature
- Humidity
- Wind Speed
- Heat Index
- Wet Bulb Temperature

The system does not use a trained crop-failure prediction model. Instead, it uses transparent statistical calculations to identify unusual environmental patterns and communicate uncertainty.

AI-assisted development tools were used during the development of the prototype, while the team reviewed and understood the implemented logic.

## 🛡️ Responsible AI & Limitations

ShambaPulse AI is designed as a decision-support and environmental monitoring prototype.

The system does **not**:

- Diagnose crop diseases
- Guarantee crop-failure predictions
- Provide guaranteed future weather predictions
- Prescribe agricultural treatment
- Claim scientifically validated crop-risk thresholds

The system communicates unusual environmental patterns and uncertainty instead of presenting uncertain outputs as guaranteed predictions.

---


## 🏗️ System Architecture

![ShambaPulse AI Architecture](ShambaPulse_Architecture%20%281%29.png)

---

## 📸 Dashboard Screenshots

### Main Dashboard

![Main Dashboard](Screenshot%202026-09-24%20114847.png)

### Environmental Intelligence

![Environmental Intelligence](Screenshot%202026-09-24%20114930.png)

### Farmer Action Intelligence

![Farmer Action Intelligence](Screenshot%202026-09-24%20114946.png)

---
## 🛠️ Technology Stack

- **Python**
- **Streamlit**
- **Python CSV module**
- **Statistical pattern analysis**
- **Conduit@Empathy environmental data**
- **HTML/CSS styling through Streamlit**

---

## 💻 Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/sviswanathanp123-dot/ShambaPulse-AI.git
cd ShambaPulse-AI
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 4. Install the required package

```bash
pip install streamlit
```

### 5. Run the application

```bash
streamlit run app.py
```

---

## 📊 Current Prototype

The current prototype provides:

- Real Conduit environmental data
- Current environmental condition monitoring
- Historical dataset summary
- Environmental trend visualization
- Anomaly monitoring
- Multi-variable pattern intelligence
- Fail-safe verification
- Environmental risk monitoring
- Farmer Action Intelligence
- Explainable monitoring signals

---

## 🔍 Example Monitoring Output

The system can combine multiple signals before increasing the monitoring level.

Example:

```text
Monitoring Status: WATCH
Environmental Risk: NORMAL
Environmental Pattern: UNUSUAL
```

This does not mean that a crop problem has been confirmed.

Instead, it indicates that the recent environmental pattern differs from the observed historical pattern and should continue to be monitored.

---

## 🚀 Future Development

Future versions could include:

- Longer-term environmental time-series analysis
- Crop-specific risk models
- Localized agricultural recommendations
- More advanced anomaly detection
- Additional environmental data sources
- Mobile-friendly farmer interfaces
- Offline-first capabilities for low-connectivity regions
- Field-level monitoring and alerts
- Model validation using agricultural ground-truth data

---

## 🎯 Impact

ShambaPulse AI aims to make environmental intelligence more understandable and actionable for farmers.

By combining real environmental observations, transparent analysis, fail-safe verification, and simple guidance, the system can help users notice unusual environmental patterns earlier and make better-informed monitoring decisions.

---

## 🧩 Why ShambaPulse AI?

Traditional environmental dashboards mainly show measurements.

ShambaPulse AI adds an intelligence layer that:

**Observes → Analyzes → Verifies → Explains → Guides**

This helps transform raw environmental data into understandable monitoring information while avoiding unsupported claims about crop failure or guaranteed predictions.

---

## 👥 Team



**Project:** ShambaPulse AI

---

## 📄 License

This project is developed as a hackathon prototype.
