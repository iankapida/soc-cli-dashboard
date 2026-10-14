import sqlite3
import json
import datetime

DB_FILE = "soc_incidents.db"

def fetch_recent_alerts():
    """Fetch incidents to package into a security notification payload."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, source_ip, failure_count, severity, timestamp FROM incidents WHERE severity = 'HIGH'")
    alerts = cursor.fetchall()
    conn.close()
    return alerts

def dispatch_webhook_alert(alert_data):
    """
    Simulate dispatching a JSON webhook payload to a SOC channel (Slack/Teams)
    or a ticketing API (Jira/ServiceNow).
    """
    inc_id, ip, failures, severity, timestamp = alert_data
    
    # Construct structured JSON payload used by enterprise SOAR tools
    payload = {
        "event_id": f"SOC-INC-{inc_id}",
        "timestamp": timestamp,
        "severity": severity,
        "indicator_of_compromise": {
            "type": "IPv4",
            "value": ip
        },
        "trigger_condition": f"Brute-force threshold breached ({failures} failures)",
        "recommended_action": "Firewall DROP rule applied",
        "status": "CONTAINED"
    }
    
    # Convert payload to strict JSON format
    json_payload = json.dumps(payload, indent=4)
    
    print(f"[*] Dispatching webhook payload for Incident # {inc_id}...")
    # In a live environment, you would use urllib.request to POST this json_payload to a webhook URL
    return json_payload

def run_notifier():
    print("[*] Initializing SOAR Webhook & Ticketing Pipeline...\n")
    alerts = fetch_recent_alerts()
    
    if not alerts:
        print("[-] No high-severity alerts found to dispatch.")
        return

    for alert in alerts:
        json_output = dispatch_webhook_alert(alert)
        
        print("\n" + "=" * 60)
        print("WEBHOOK ALERT & TICKET PAYLOAD DISPATCHED:")
        print("=" * 60)
        print(json_output)
        print("=" * 60 + "\n")

if __name__ == "__main__":
    run_notifier()
