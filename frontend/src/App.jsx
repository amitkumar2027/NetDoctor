import { useState } from "react";
import axios from "axios";

const API_URL = "http://localhost:8000";

function MetricCard({ title, value, unit }) {
  return (
    <div className="metric-card">
      <span>{title}</span>
      <strong>{value ?? "--"} {unit ?? ""}</strong>
    </div>
  );
}

export default function App() {
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("Ready to diagnose your connection.");

  async function startDiagnosis() {
    setLoading(true);
    setMessage("Starting network diagnosis...");

    try {
      const response = await axios.post(`${API_URL}/diagnosis/start`);
      setMessage(response.data.message);
    } catch (error) {
      setMessage("Backend is not reachable. Start the FastAPI server first.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="app">
      <header>
        <div>
          <p className="eyebrow">NETWORK INTELLIGENCE</p>
          <h1>NetDoctor</h1>
          <p>Find out why your Internet is slow or unstable.</p>
        </div>

        <button onClick={startDiagnosis} disabled={loading}>
          {loading ? "Diagnosing..." : "Run Diagnosis"}
        </button>
      </header>

      <section className="health">
        <div>
          <p className="label">Internet Health</p>
          <div className="score">--<small>/100</small></div>
          <p>{message}</p>
        </div>

        <div className="status">WAITING</div>
      </section>

      <section className="metrics">
        <MetricCard title="Latency" value="--" unit="ms" />
        <MetricCard title="Jitter" value="--" unit="ms" />
        <MetricCard title="Packet Loss" value="--" unit="%" />
        <MetricCard title="DNS Latency" value="--" unit="ms" />
        <MetricCard title="HTTP Response" value="--" unit="ms" />
        <MetricCard title="Download" value="--" unit="Mbps" />
      </section>

      <section className="diagnosis">
        <p className="label">DIAGNOSIS</p>
        <h2>No diagnosis yet</h2>
        <p>
          Run a diagnostic test to collect network measurements and identify
          the probable problem area.
        </p>
      </section>
    </div>
  );
}
