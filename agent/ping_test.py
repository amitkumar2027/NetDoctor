import platform
import re
import statistics
import subprocess


def run_ping_test(host="8.8.8.8", count=10):
    system = platform.system()

    if system == "Windows":
        command = ["ping", "-n", str(count), host]
    else:
        command = ["ping", "-c", str(count), host]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=30,
        )

        output = result.stdout

        if system == "Windows":
            pattern = r"time[=<]\s*(\d+(?:\.\d+)?)\s*ms"
        else:
            pattern = r"time[=<]\s*(\d+(?:\.\d+)?)\s*ms"

        values = [float(x) for x in re.findall(pattern, output)]

        successful = len(values)
        packet_loss = ((count - successful) / count) * 100

        if not values:
            return {
                "host": host,
                "average_latency_ms": None,
                "packet_loss_percent": round(packet_loss, 2),
                "jitter_ms": None,
                "status": "failed",
            }

        average = statistics.mean(values)

        # Standard deviation gives a useful first approximation of jitter.
        jitter = statistics.stdev(values) if len(values) > 1 else 0

        return {
            "host": host,
            "average_latency_ms": round(average, 2),
            "packet_loss_percent": round(packet_loss, 2),
            "jitter_ms": round(jitter, 2),
            "status": "success",
        }

    except (subprocess.SubprocessError, OSError):
        return {
            "host": host,
            "average_latency_ms": None,
            "packet_loss_percent": 100.0,
            "jitter_ms": None,
            "status": "failed",
        }
