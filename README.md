# 🩺 NetDoctor — Intelligent Internet Diagnosis Platform

> **Speed tests tell you HOW FAST. NetDoctor tells you WHY IT'S BAD.**

NetDoctor is an intelligent Internet diagnosis platform designed to identify **why an Internet connection is slow, unstable, or unreliable**.

Unlike traditional speed-test applications that primarily report download/upload speed, NetDoctor performs a **multi-layer network diagnosis** by analyzing latency, jitter, packet loss, DNS performance, HTTP response time, traceroute paths, system/network information, and historical performance.

The collected data is correlated by a **Diagnosis Engine** to determine the most likely source of a network problem and provide understandable recommendations to the user.

---

## 🚀 Key Features

### 🔍 Multi-Layer Network Diagnosis

NetDoctor analyzes Internet connectivity at multiple levels:

* 📡 **Latency / Ping**
* 📊 **Jitter**
* 📦 **Packet Loss**
* 🌐 **DNS Resolution Performance**
* ⚡ **HTTP/HTTPS Response Time**
* 🛣️ **Traceroute / Network Path**
* ⬇️ **Download Speed**
* ⬆️ **Upload Speed**
* 💻 **Local System & Network Information**
* 📈 **Historical Performance**

---

### 🧠 Intelligent Failure-Domain Detection

Instead of simply saying:

> "Your Internet is slow."

NetDoctor attempts to answer:

> **"Where is the problem?"**

The system analyzes multiple measurements to identify a probable failure domain such as:

```text
User Device
     ↓
Local Network / Wi-Fi
     ↓
Router / Gateway
     ↓
DNS
     ↓
ISP Network
     ↓
Upstream Route
     ↓
Destination Server
```

Possible diagnosis examples:

* High local latency → Possible Wi-Fi/LAN issue
* High packet loss → Possible connectivity problem
* High DNS latency → Possible DNS problem
* Normal DNS but slow HTTP → Possible destination/server issue
* Increased latency at specific traceroute hops → Possible routing/ISP-path issue
* Good speed but high jitter → Possible unstable connection

> The system uses multiple signals rather than relying on a single measurement.

---

## 🎯 Problem Statement

Traditional Internet speed-test applications mainly answer:

> **"How fast is my Internet?"**

However, users often experience problems such as:

* Websites taking too long to load
* Online games having high ping
* Video calls freezing
* Random packet loss
* DNS resolution delays
* Slow performance for specific websites
* Internet working normally at some times and poorly at others

A speed test may show a low speed or high latency, but it usually does not explain **the underlying reason**.

NetDoctor aims to bridge this gap by performing **automated network diagnosis and failure-domain analysis**.

---

## 💡 Project Objectives

The major objectives of NetDoctor are:

1. Measure important network performance parameters.
2. Analyze different layers of the user's network connection.
3. Identify the probable source of network degradation.
4. Correlate multiple network measurements.
5. Compare current performance with historical baselines.
6. Provide an understandable diagnosis instead of raw numbers.
7. Generate actionable recommendations.
8. Generate an ISP-ready diagnostic report.
9. Introduce machine-learning-based anomaly detection in later stages.

---

# 🏗️ System Architecture

```text
                         ┌──────────────────────┐
                         │        USER          │
                         │   React Dashboard    │
                         └──────────┬───────────┘
                                    │
                              REST / JSON
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      FastAPI         │
                         │       Backend        │
                         └──────────┬───────────┘
                                    │
                                    ▼
                    ┌──────────────────────────────┐
                    │     Diagnostic Agent         │
                    │                              │
                    │  ┌────────┐  ┌───────────┐   │
                    │  │  Ping  │  │    DNS    │   │
                    │  └────────┘  └───────────┘   │
                    │                              │
                    │  ┌────────┐  ┌───────────┐   │
                    │  │  HTTP  │  │ Traceroute│   │
                    │  └────────┘  └───────────┘   │
                    │                              │
                    │  ┌────────┐  ┌───────────┐   │ 
                    │  │ Speed  │  │System Info│   │
                    │  └────────┘  └───────────┘   │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                         ┌──────────────────────┐
                         │     PostgreSQL       │
                         │      Database        │
                         └──────────┬───────────┘
                                    │
                                    ▼
                    ┌──────────────────────────────┐
                    │    Diagnosis Engine          │
                    │                              │
                    │  Rules + Correlation         │
                    │  Historical Baseline         │
                    │  ML / Anomaly Detection      │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                         ┌──────────────────────┐
                         │ Diagnosis + Score    │
                         │ Recommendations      │
                         │ Reports              │
                         └──────────────────────┘
```

---

# 🧩 Major Components

## 1. Diagnostic Agent

The Diagnostic Agent is responsible for collecting real network measurements from the user's system.

### Components

| Module               | Purpose                                   |
| -------------------- | ----------------------------------------- |
| `ping_test.py`       | Measures latency, packet loss and jitter  |
| `dns_test.py`        | Measures DNS resolution performance       |
| `http_test.py`       | Measures HTTP/HTTPS response time         |
| `traceroute_test.py` | Analyzes network path                     |
| `system_info.py`     | Collects local network/system information |
| `main.py`            | Runs and combines diagnostic tests        |

The agent produces structured data that can be consumed by the backend.

Example:

```json
{
  "latency_ms": 42,
  "packet_loss_percent": 2.5,
  "jitter_ms": 8.4,
  "dns_latency_ms": 31,
  "http_response_ms": 185
}
```

---

# ⚙️ Diagnosis Engine

The Diagnosis Engine is the core intelligence of NetDoctor.

Initially, the project uses **rule-based diagnosis**.

For example:

```text
IF packet_loss > threshold
AND latency > threshold
→ Possible connectivity issue
```

Another example:

```text
IF DNS latency is high
AND HTTP latency is normal after resolution
→ Possible DNS performance issue
```

As the project develops, historical data can be used to build:

* Personalized baselines
* Anomaly detection
* Network health scoring
* ML-based diagnosis
* Pattern recognition

---

# 📊 Internet Health Score

NetDoctor can generate an overall network health score based on multiple parameters.

Example:

```text
Internet Health
────────────────────────

72 / 100

Latency       ████████░░
Jitter        ███████░░░
Packet Loss   █████████░
DNS           ████████░░
HTTP          ██████░░░░
Stability     ███████░░░
```

The score is intended to provide a quick overview while the detailed diagnosis explains **why the score is low or high**.

---

# 🌐 Destination-Specific Diagnosis

One important capability of NetDoctor is checking whether the problem is:

### Global

```text
All destinations are slow
        ↓
Possible local / ISP problem
```

### Destination-Specific

```text
Google       → Good
YouTube      → Good
Website A    → Slow
Website B    → Good

        ↓

Possible destination-specific
routing/server issue
```

This helps distinguish between a general Internet problem and an issue affecting a particular service or route.

---

# 📈 Historical Baseline

NetDoctor can store previous diagnostic results in PostgreSQL.

Example:

```text
Monday
Latency: 25 ms

Tuesday
Latency: 27 ms

Wednesday
Latency: 29 ms

Today
Latency: 92 ms
```

The system can detect:

> Current latency is significantly higher than the user's normal baseline.

This allows NetDoctor to identify **degradation relative to the user's own network history**, rather than relying only on fixed thresholds.

---

# 🧠 Machine Learning — Future Phase

Machine learning will be introduced after enough diagnostic data has been collected.

Potential applications include:

* Anomaly Detection
* Network Performance Prediction
* Failure Classification
* Personalized Baseline Detection
* Network Health Prediction

Possible technologies:

```text
Python
   ↓
Pandas
   ↓
Scikit-learn
   ↓
Feature Engineering
   ↓
Anomaly Detection / Classification
```

The ML component is intentionally planned as a later phase so that the initial system can be developed and validated independently.

---

# 🛠️ Technology Stack

## Frontend

* React
* Vite
* JavaScript / JSX
* CSS
* Axios
* Charting library

## Backend

* Python
* FastAPI
* REST API

## Network Diagnostics

* Python
* `ping`
* `traceroute` / `tracert`
* `dnspython`
* `requests` / HTTP client
* `psutil`

## Database

* PostgreSQL

## Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn

## DevOps / Deployment

* Docker
* Docker Compose
* GitHub
* GitHub Actions
* AWS *(planned)*

---

# 📁 Project Structure

```text
netdoctor/
│
├── agent/
│   ├── main.py
│   ├── ping_test.py
│   ├── dns_test.py
│   ├── http_test.py
│   ├── traceroute_test.py
│   ├── system_info.py
│   └── requirements.txt
│
├── backend/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── src/
│       ├── main.jsx
│       ├── App.jsx
│       └── styles.css
│
├── database/
│   ├── schema.sql
│   └── README.md
│
├── ml/
│   ├── train.py
│   └── README.md
│
├── docs/
│   ├── architecture.md
│   └── team-work.md
│
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

---

# 🚀 Getting Started

## Prerequisites

Install the following:

* Python 3.10+
* Node.js 18+
* npm
* PostgreSQL
* Git

---

## 1. Clone the Repository

```bash
git clone https://github.com/amitkumar2027/NetDoctor.git

cd netdoctor
```

---

# 2. Run the Diagnostic Agent

Navigate to the agent:

```bash
cd agent
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

The agent will execute the available diagnostic tests and return structured results.

---

# 3. Run the Backend

Open another terminal:

```bash
cd backend
```

Create/activate a Python environment and install dependencies:

```bash
pip install -r requirements.txt
```

Start FastAPI:

```bash
uvicorn main:app --reload
```

Backend will be available locally at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 4. Run the React Frontend

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Open the URL shown by Vite in your browser.

---

# 🗄️ Database Setup

Create a PostgreSQL database for NetDoctor.

Then execute:

```text
database/schema.sql
```

The initial database contains tables for:

* Users
* Diagnosis Sessions
* Measurements
* Traceroute Hops

The schema can be extended as new diagnostic features are implemented.

---

# 🔬 Example Diagnosis Flow

A typical NetDoctor diagnosis follows this process:

```text
1. User starts diagnosis
          ↓
2. Diagnostic Agent starts
          ↓
3. Ping test
          ↓
4. DNS test
          ↓
5. HTTP/HTTPS test
          ↓
6. Traceroute
          ↓
7. System/network information
          ↓
8. Results sent to backend
          ↓
9. Results stored in PostgreSQL
          ↓
10. Diagnosis Engine analyzes measurements
          ↓
11. Health score generated
          ↓
12. Probable problem identified
          ↓
13. Recommendations generated
          ↓
14. Results displayed on React dashboard
```

---

# 👥 Team Structure

This project is designed for a **4-member development team**.

### Member 1 — Network Diagnostic Agent

Responsible for:

* Ping
* DNS
* HTTP/HTTPS
* Traceroute
* System/network information
* Diagnostic data collection

### Member 2 — Backend & Database

Responsible for:

* FastAPI
* REST APIs
* PostgreSQL
* Database schema
* Agent-backend integration

### Member 3 — Frontend

Responsible for:

* React dashboard
* Diagnostic UI
* Health score
* Charts
* Historical results
* Recommendations interface

### Member 4 — Diagnosis, ML & Deployment

Responsible for:

* Diagnosis rules
* Health-score logic
* Historical baseline
* ML/anomaly detection
* Docker
* Deployment
* CI/CD

---

# 🗺️ Development Roadmap

## Phase 1 — Network Agent

* [x] Project structure
* [ ] Ping measurement
* [ ] DNS measurement
* [ ] HTTP measurement
* [ ] Traceroute
* [ ] System information
* [ ] Structured JSON output

## Phase 2 — Backend

* [ ] FastAPI setup
* [ ] Diagnostic API
* [ ] Agent integration
* [ ] Result API
* [ ] Error handling

## Phase 3 — Database

* [ ] PostgreSQL setup
* [ ] Store diagnostic sessions
* [ ] Store measurements
* [ ] Store traceroute information
* [ ] Historical queries

## Phase 4 — React Dashboard

* [ ] Dashboard
* [ ] Start diagnosis button
* [ ] Live diagnostic status
* [ ] Health score
* [ ] Metric cards
* [ ] Charts
* [ ] Diagnosis explanation

## Phase 5 — Intelligent Diagnosis

* [ ] Rule engine
* [ ] Failure-domain classification
* [ ] Recommendation engine
* [ ] Historical baseline
* [ ] Anomaly detection

## Phase 6 — Advanced Features

* [ ] Destination comparison
* [ ] ISP diagnostic report
* [ ] PDF report
* [ ] ML model
* [ ] Docker deployment
* [ ] Cloud deployment
* [ ] Monitoring

---

# 🔮 Future Scope

Possible future improvements include:

### 🤖 AI/ML Diagnosis

Use machine learning to classify network failures from historical diagnostic patterns.

### 📱 Mobile Application

Provide network diagnosis through a mobile application.

### 🌍 Distributed Monitoring

Allow users to compare network performance from different geographic locations.

### 📄 ISP Complaint Generator

Generate a structured report containing:

```text
Diagnosis Time
Latency
Packet Loss
Jitter
DNS Performance
Traceroute
HTTP Performance
Historical Comparison
Probable Cause
Evidence
```

The report can be shared with an ISP support team.

### 🔔 Continuous Monitoring

Instead of running a diagnosis manually, NetDoctor can periodically monitor the connection and detect degradation automatically.

---

# 📌 Why NetDoctor?

Traditional tools generally answer:

```text
Download Speed → 85 Mbps
Upload Speed   → 20 Mbps
Ping           → 45 ms
```

NetDoctor aims to answer:

```text
Internet Health → 72/100

Probable Issue:
High latency and packet loss

Likely Domain:
Network path / ISP

Evidence:
• Latency above baseline
• Packet loss detected
• DNS performing normally
• Multiple destinations affected

Recommendation:
Run additional path diagnostics
and monitor the connection.
```

The goal is to convert **raw network measurements into understandable diagnosis and evidence**.

---

# ⚠️ Important Note

Network diagnosis is inherently uncertain because some routers and network devices may intentionally deprioritize or block diagnostic packets such as ICMP.

Therefore, NetDoctor should not declare:

> "Your ISP is definitely responsible."

based on a single measurement.

Instead, the system should report:

> **"The available evidence suggests a possible ISP/path-related issue."**

and provide the measurements supporting that conclusion.

---

# 📜 Project Status

**Status:** 🚧 Active Development

NetDoctor is being developed incrementally, starting with the network diagnostic agent and progressing toward a complete intelligent Internet diagnosis platform.

---

# 👨‍💻 Contributors

| Member   | Responsibility             |
| -------- | -------------------------- |
| Member 1 | Network Diagnostic Agent   |
| Member 2 | Backend & Database         |
| Member 3 | React Frontend             |
| Member 4 | Diagnosis, ML & Deployment |

---

# ⭐ Vision

NetDoctor aims to make network troubleshooting more understandable for ordinary users.

Instead of asking:

> **"Why is my Internet slow?"**

the user should be able to open NetDoctor and get:

> **"Your connection is currently unstable. Packet loss and latency are elevated compared with your normal baseline. DNS performance is normal, while the network path shows increased delay. The evidence suggests a possible connectivity or routing issue."**

**Measure → Correlate → Diagnose → Explain → Recommend**

---

## 📄 License

This project is developed for academic and educational purposes.
