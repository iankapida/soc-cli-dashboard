# soc_metrics.py
import os
import json

def calculate_soc_metrics():
    print("[*] Calculating SOC Operations Metrics...")
    
    # Check blocklist count
    blocked_count = 0
    if os.path.exists("firewall_deny.list"):
        with open("firewall_deny.list", "r") as f:
            lines = f.readlines()
            # Filter out comment lines
            blocked_count = sum(1 for line in lines if not line.startswith("#") and line.strip())
            
    # Check archive count
    archive_count = 0
    if os.path.exists("archives"):
        archive_count = len(os.listdir("archives"))
        
    metrics = {
        "active_threat_blocks": blocked_count,
        "total_log_archives": archive_count,
        "system_status": "OPTIMAL",
        "automation_pipeline": "ACTIVE"
    }
    
    print("-" * 40)
    print(" === SOC OPERATIONAL DASHBOARD METRICS ===")
    print(json.dumps(metrics, indent=4))
    print("-" * 40)

if __name__ == "__main__":
    calculate_soc_metrics()
