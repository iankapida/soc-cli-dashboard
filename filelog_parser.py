import re
import json
import os

# Step 1: Simulate writing raw log telemetry to a local file on disk
log_filename = "auth_telemetry.log"
sample_logs = [
    "2026-09-12 14:10:01 [AUTH_FAIL] Root login attempt failed from 203.0.113.50",
    "2026-09-12 14:10:05 [AUTH_SUCCESS] Admin login successful from 192.168.1.15",
    "2026-09-12 14:11:00 [ALERT] Unauthorized brute-force burst from 198.51.100.22"
]

print(f"[*] Writing raw telemetry to local storage: {log_filename}")
with open(log_filename, "w") as f:
    for log in sample_logs:
        f.write(log + "\n")

# Step 2: Professional File Handling & SIEM Normalization
ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
structured_alerts = []

print(f"[*] Opening and reading file handle from disk: {log_filename}")
with open(log_filename, "r") as f:
    for line in f:
        if "FAIL" in line or "ALERT" in line:
            ips = re.findall(ip_pattern, line)
            alert_payload = {
                "timestamp": line.split("[")[0].strip(),
                "event_type": line.split("]")[0].replace("[", "").strip(),
                "source_ip": ips[0] if ips else "Unknown",
                "raw_message": line.strip(),
                "severity": "HIGH" if "ALERT" in line else "MEDIUM"
            }
            structured_alerts.append(alert_payload)

# Step 3: Export Structured Telemetry to JSON (SIEM Forwarder Format)
output_file = "siem_export.json"
with open(output_file, "w") as jf:
    json.dump(structured_alerts, jf, indent=4)

print(f"[+] Successfully exported {len(structured_alerts)} alerts to structured JSON: {output_file}")
print("[+] Previewing generated JSON payload schema:")
print(json.dumps(structured_alerts[0], indent=2))
