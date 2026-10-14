# Simulated firewall or server log data
log_data = [
    "INFO: User admin logged in successfully from 192.168.1.10",
    "WARNING: Failed password attempt for root from 203.0.113.50",
    "INFO: User john connected via SSH",
    "WARNING: Failed password attempt for admin from 203.0.113.50",
    "ALERT: Unauthorized access detected from 198.51.100.22"
]

print("[*] Scanning logs for security threats...")
for line in log_data:
    if "WARNING" in line or "ALERT" in line:
        print(f"[!] Flagged Event Found: {line}")
