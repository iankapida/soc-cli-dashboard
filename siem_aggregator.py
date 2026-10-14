# siem_aggregator.py
import os
import json
from datetime import datetime

def aggregate_siem_data():
    print("[*] Running Centralized SIEM Log Aggregation...")
    
    # Gather workspace telemetry
    artifacts = {
        "active_log": os.path.exists("suspect_traffic.log"),
        "firewall_deny_list": os.path.exists("firewall_deny.list"),
        "archives_count": len(os.listdir("archives")) if os.path.exists("archives") else 0,
        "honeytoken_active": os.path.exists("aws_credentials_backup.json")
    }
    
    report = {
        "siem_engine": "SOC-CLI-Dashboard",
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC'),
        "monitored_artifacts": artifacts,
        "cluster_status": "SECURE",
        "analyst": "Tier-1 SOC Analyst"
    }
    
    output_filename = "siem_master_report.json"
    with open(output_filename, "w") as f:
        json.dump(report, f, indent=4)
        
    print("-" * 50)
    print(" >>> SIEM MASTER AGGREGATION COMPLETE <<<")
    print(json.dumps(report, indent=4))
    print("-" * 50)
    print(f"    [+] Master report saved to {output_filename}")

if __name__ == "__main__":
    aggregate_siem_data()
