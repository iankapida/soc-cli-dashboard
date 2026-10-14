# report_generator.py
import json
from datetime import datetime, timezone

def generate_incident_report():
    print("[*] Compiling SOC Incident Report...")
    
    incident_data = {
        "incident_id": "INC-2026-0884",
        "timestamp": datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
        "analyst": "SOC-Tier1-Analyst",
        "target_file": "suspect_traffic.log",
        "severity": "HIGH",
        "indicators_of_compromise": {
            "attacker_ip": "192.168.1.50",
            "detected_behaviors": [
                "Unauthorized access attempt",
                "Failed password attempt for root",
                "Port scan detected",
                "Brute-force threshold crossed (2+ failures)"
            ]
        },
        "recommended_action": "Isolate host IP 192.168.1.50 at firewall level and initiate credential rotation."
    }
    
    report_filename = "incident_report_884.json"
    with open(report_filename, "w") as f:
        json.dump(incident_data, f, indent=4)
        
    print(f"    [+] Incident report successfully generated: {report_filename}")

if __name__ == "__main__":
    generate_incident_report()
