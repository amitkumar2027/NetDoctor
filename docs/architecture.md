# NetDoctor Architecture

```text
                    USER
                      |
                      v
              React Frontend
                      |
                 REST API
                      |
                      v
               FastAPI Backend
                      |
              +-------+-------+
              |               |
              v               v
       Python Agent        PostgreSQL
              |
       +------+------+------+
       |      |      |      |
      Ping   DNS    HTTP  Traceroute
       |
   Packet Loss / Jitter
              |
              v
       Diagnosis Engine
              |
              v
     Diagnosis + Recommendation
              |
              v
        React Dashboard
```

## Core idea

The project should not only report measurements. It should correlate multiple measurements and explain the probable failure domain.

Potential failure domains:

- Local device/network
- Router/Wi-Fi
- DNS
- ISP
- Upstream route
- Destination-specific problem
