# Simulated access logs tracking failed logins
logs = [
    "FAIL 192.168.1.50",
    "SUCCESS 192.168.1.10",
    "FAIL 192.168.1.50",
    "FAIL 192.168.1.50",
    "FAIL 192.168.1.20"
]

ip_counts = {}

print("[*] Analyzing logs for threshold breaches...")
for entry in logs:
    if "FAIL" in entry:
        ip = entry.split()[1]
        ip_counts[ip] = ip_counts.get(ip, 0) + 1

# Flag IPs exceeding a threshold of 3 failures
for ip, count in ip_counts.items():
    if count >= 3:
        print(f"[!] ALERT: IP {ip} locked out after {count} failed attempts!")
