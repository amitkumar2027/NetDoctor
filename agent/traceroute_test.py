import platform
import subprocess


def run_traceroute(destination="google.com"):
    system = platform.system()

    if system == "Windows":
        command = ["tracert", "-d", destination]
    else:
        command = ["traceroute", "-n", destination]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=60,
        )

        return {
            "destination": destination,
            "output": result.stdout,
            "status": "success" if result.returncode == 0 else "partial",
        }

    except (subprocess.SubprocessError, OSError):
        return {
            "destination": destination,
            "output": "",
            "status": "failed",
        }
