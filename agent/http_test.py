import time
import requests


def run_http_test(url="https://www.google.com"):
    try:
        start = time.perf_counter()

        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True,
        )

        end = time.perf_counter()

        return {
            "url": url,
            "status_code": response.status_code,
            "response_time_ms": round((end - start) * 1000, 2),
            "status": "success",
        }

    except requests.RequestException:
        return {
            "url": url,
            "status_code": None,
            "response_time_ms": None,
            "status": "failed",
        }
