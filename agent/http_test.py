import time
import requests


def test_http(url="https://www.google.com"):

    try:

        start = time.perf_counter()

        response = requests.get(
            url,
            timeout=5
        )

        end = time.perf_counter()

        response_time = (end - start) * 1000

        return {
            "url": url,
            "status_code": response.status_code,
            "response_time_ms": round(response_time, 2),
            "status": "success"
        }

    except requests.RequestException as e:

        return {
            "url": url,
            "status_code": None,
            "response_time_ms": None,
            "status": "failed"
        }