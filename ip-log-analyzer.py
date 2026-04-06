import time
from collections import defaultdict

# IP logları
ip_requests = defaultdict(int)

# Limit (kaç istekten sonra uyarı versin)
THRESHOLD = 5

def log_ip(ip):
    ip_requests[ip] += 1
    print(f"[LOG] {ip} -> {ip_requests[ip]} request")

    if ip_requests[ip] >= THRESHOLD:
        alert(ip)

def alert(ip):
    print(f"[ALERT] Suspicious activity detected from IP: {ip}")

# Test simülasyonu
test_ips = ["192.168.1.1", "192.168.1.2", "192.168.1.1", 
            "192.168.1.1", "192.168.1.1", "192.168.1.1"]

for ip in test_ips:
    log_ip(ip)
    time.sleep(1)