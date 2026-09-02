import json
from datetime import datetime

from ping_test import run_ping_test
from dns_test import run_dns_test
from http_test import run_http_test


def run_diagnosis():
    print("Starting NetDoctor network diagnosis...")

    result = {
        "timestamp": datetime.now().isoformat(),
        "ping": run_ping_test(),
        "dns": run_dns_test(),
        "http": run_http_test(),
    }

    return result


if __name__ == "__main__":
    result = run_diagnosis()

    print("\nDiagnosis data:")
    print(json.dumps(result, indent=4))
