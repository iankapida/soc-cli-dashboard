import re
from collections import Counter

# Simulated log data (representing authentication or firewall logs)
log_data = [
    "2026-09-15 08:12:01 - INFO - Successful login from 192.168.1.10",
    "2026-09-15 08:14:22 - FAILED - Invalid password for root from 203.0.113.50",
    "2026-09-15 08:14:25 - FAILED - Invalid password for root from 203.0.113.50",
    "2026-09-15 08:14:28 - FAILED - Invalid password for root from 203.0.113.50",
    "2026-09-15 08:15:01 - INFO - Successful login from 192.168.1.15",
    "2026-09-15 08:18:40 - FAILED - Invalid password for admin from 198.51.100.23",
]

def analyze_failed_logins(logs):
    ip_pattern = r'from\s+(\d{1,3}(?:\.\d{1,3}){3})'
    failed_ips = []

    print("[*] Analyzing logs for security anomalies...\n")

    for line in logs:
        if "FAILED" in line:
            match = re.search(ip_pattern, line)
            if match:
                ip = match.group(1)
                failed_ips.append(ip)

    # Count occurrences to flag potential brute-force attempts
    ip_counts = Counter(failed_ips)
    
    for ip, count in ip_counts.items():
        if count >= 3:
            print(f"[!] ALERT: Potential brute-force detected from IP {ip} ({count} failed attempts)")
        else:
            print(f"[-] Notice: Failed attempt from IP {ip} ({count} attempt)")

if __name__ == "__main__":
    analyze_failed_logins(log_data)
