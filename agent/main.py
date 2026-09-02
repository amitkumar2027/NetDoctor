from ping_test import ping_host
from dns_test import test_dns
from http_test import test_http


def run_diagnosis():

    print("=" * 50)
    print("        NETDOCTOR DIAGNOSTIC AGENT")
    print("=" * 50)

    print("\n[1] Running Ping Test...")

    ping_result = ping_host(
        host="8.8.8.8",
        count=10
    )

    print(ping_result)

    print("\n[2] Running DNS Tests...")

    dns_results = test_dns(
        domain="google.com"
    )

    for result in dns_results:
        print(result)

    print("\n[3] Running HTTP Test...")

    http_result = test_http(
        "https://www.google.com"
    )

    print(http_result)

    print("\n" + "=" * 50)
    print("          DIAGNOSIS DATA COLLECTED")
    print("=" * 50)


if __name__ == "__main__":
    run_diagnosis()