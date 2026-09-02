-- NetDoctor PostgreSQL Database

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS diagnosis_sessions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    health_score INTEGER,
    diagnosis VARCHAR(255),
    confidence DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS measurements (
    id SERIAL PRIMARY KEY,
    session_id INTEGER NOT NULL REFERENCES diagnosis_sessions(id) ON DELETE CASCADE,
    metric_name VARCHAR(100) NOT NULL,
    metric_value DECIMAL(12,4),
    unit VARCHAR(30),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS traceroute_hops (
    id SERIAL PRIMARY KEY,
    session_id INTEGER NOT NULL REFERENCES diagnosis_sessions(id) ON DELETE CASCADE,
    hop_number INTEGER NOT NULL,
    ip_address VARCHAR(100),
    latency_ms DECIMAL(12,4),
    packet_loss DECIMAL(5,2)
);
