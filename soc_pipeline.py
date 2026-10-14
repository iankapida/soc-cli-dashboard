import re
import json

# Step 1: Raw telemetry log ingestion (Simulating a SIEM log stream)
raw_log_stream = [
    "INFO: User admin logged in successfully from 192.168.1.10",
    "WARNING: Multiple failed logins observed from IP 192.168.100.45 targeting SSH",
    "INFO: System health check normal."
]

# Simulated threat intelligence database lookup function
def check_threat_intel(ip_address):
    # In production, this would be an active REST API query
    kb = {
        "192.168.100.45": {"score": 88, "status": "Malicious", "ttp": "T1110 - Brute Force"},
        "192.168.1.10": {"score": 2, "status": "Clean", "ttp": "None"}
    }
    return kb.get(ip_address, {"score": 0, "status": "Unknown", "ttp": "None"})

print("[*] Initializing Automated SOC Triage Pipeline...")
ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

for log in raw_log_stream:
    if "WARNING" in log or "ERROR" in log:
        print(f"\n[!] Alert Triggered in Log: {log}")
        
        # Step 2: Extract IoC using Regular Expressions
        extracted_ips = re.findall(ip_pattern, log)
        
        for ip in extracted_ips:
            print(f"    -> Extracted Target IP: {ip}")
            
            # Step 3: Enrich with Threat Intelligence API data
            intel = check_threat_intel(ip)
            print(f"    -> Threat Intel Score: {intel['score']}/100 [{intel['status']}]")
            print(f"    -> MITRE ATT&CK Mapping: {intel['ttp']}")
            
            # Step 4: Decision Engine & Automated Playbook Trigger
            if intel['score'] >= 75:
                print(f"    -> [AUTOMATED ACTION]: Threat score exceeds threshold. Isolating host {ip} and pushing firewall block rule.")
            else:
                print(f"    -> [STATUS]: Indicator logged for baseline monitoring.")

print("\n[+] Pipeline execution complete. Incident queue updated.")
