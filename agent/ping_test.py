import platform
import subprocess
import statistics
import re


def ping_host(host="8.8.8.8", count=10):
    system = platform.system().lower()

    if system == "windows":
        command = ["ping", "-n", str(count), host]
    else:
        command = ["ping", "-c", str(count), host]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    output = result.stdout

    latencies = []

    if system == "windows":
        matches = re.findall(r"time[=<]\s*(\d+)\s*ms", output)
    else:
        matches = re.findall(r"time[=<]\s*(\d+(?:\.\d+)?)\s*ms", output)

    for value in matches:
        latencies.append(float(value))

    successful = len(latencies)

    packet_loss = ((count - successful) / count) * 100

    if latencies:
        average_latency = statistics.mean(latencies)

        if len(latencies) > 1:
            jitter = statistics.stdev(latencies)
        else:
            jitter = 0
    else:
        average_latency = None
        jitter = None

    return {
        "host": host,
        "average_latency_ms": round(average_latency, 2)
        if average_latency is not None else None,

        "packet_loss_percent": round(packet_loss, 2),

        "jitter_ms": round(jitter, 2)
        if jitter is not None else None,

        "samples": successful
    }