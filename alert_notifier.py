# alert_notifier.py
import json
from datetime import datetime, timezone

def dispatch_soc_alert(incident_file="incident_report_884.json"):
    print("[*] Loading incident report for emergency dispatch...")
    
    try:
        with open(incident_file, "r") as f:
            incident = json.load(f)
    except FileNotFoundError:
        print(f"    [!] Error: Incident report {incident_file} not found.")
        return

    # Simulate formatting a secure webhook payload for Slack/Webex
    payload = {
        "msg_type": "HIGH_SEVERITY_SECURITY_ALERT",
        "incident_id": incident["incident_id"],
        "timestamp": incident["timestamp"],
        "summary": f"Attack detected from {incident['indicators_of_compromise']['attacker_ip']}",
        "severity": incident["severity"],
        "action_taken": incident["recommended_action"]
    }
    
    print("-" * 50)
    print(" >>> DISPATCHING SECURE WEBHOOK NOTIFICATION <<<")
    print(json.dumps(payload, indent=4))
    print("-" * 50)
    print("    [+] Alert successfully dispatched to SOC Incident Channel.")

if __name__ == "__main__":
    dispatch_soc_alert()
