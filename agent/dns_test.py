import time

import dns.resolver


DNS_SERVERS = {
    "Cloudflare": "1.1.1.1",
    "Google": "8.8.8.8",
    "Quad9": "9.9.9.9",
}


def run_dns_test(domain="google.com"):
    results = []

    for name, server in DNS_SERVERS.items():
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [server]
        resolver.timeout = 3
        resolver.lifetime = 3

        try:
            start = time.perf_counter()
            resolver.resolve(domain, "A")
            end = time.perf_counter()

            latency = (end - start) * 1000

            results.append({
                "server": name,
                "ip": server,
                "latency_ms": round(latency, 2),
                "status": "success",
            })

        except Exception:
            results.append({
                "server": name,
                "ip": server,
                "latency_ms": None,
                "status": "failed",
            })

    return {
        "domain": domain,
        "results": results,
    }
