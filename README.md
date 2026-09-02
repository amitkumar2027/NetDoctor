# NetDoctor 🩺🌐

## Intelligent Internet Fault Diagnosis Platform

NetDoctor is a full-stack project that goes beyond a normal speed test. It collects network measurements such as latency, jitter, packet loss, DNS latency and HTTP response time, then analyzes them to explain the probable reason behind poor Internet performance.

### Project Flow

React Frontend
        ↓
FastAPI Backend
        ↓
Python Diagnostic Agent
        ↓
Network Tests
        ↓
PostgreSQL Database
        ↓
Diagnosis Engine / ML
        ↓
Diagnosis + Recommendation
        ↓
React Dashboard

### Team Structure

- Member 1: Network Diagnostic Agent
- Member 2: FastAPI Backend + PostgreSQL
- Member 3: React Frontend
- Member 4: Diagnosis Engine + ML + Deployment

### Development Order

1. Make the Python diagnostic agent work.
2. Connect the agent with FastAPI.
3. Store measurements in PostgreSQL.
4. Build the React dashboard.
5. Add diagnosis rules.
6. Add historical baseline and ML.
7. Add Docker/AWS later.

### Important

Do not commit `.env`, passwords, API keys or generated data.
