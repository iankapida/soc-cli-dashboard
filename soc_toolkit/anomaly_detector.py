import datetime

# Baseline normal operating hours for administrative access
NORMAL_START_HOUR = 8
NORMAL_END_HOUR = 18

# Simulated authentication logs with timestamps
AUTH_LOGS = [
    {"user": "admin", "timestamp": "2026-09-18 10:15:22", "source_ip": "192.168.1.50"},
    {"user": "root",  "timestamp": "2026-09-18 03:42:11", "source_ip": "45.33.32.156"}, # Suspicious off-hours
    {"user": "alice", "timestamp": "2026-09-18 14:20:05", "source_ip": "192.168.1.55"}
]

def analyze_behavior(log_entry):
    """Check if login timestamp deviates from normal baseline hours."""
    dt_obj = datetime.datetime.strptime(log_entry["timestamp"], "%Y-%m-%d %H:%M:%S")
    hour = dt_obj.hour
    
    print(f"[*] Analyzing activity for user '{log_entry['user']}' at {dt_obj.time()}...")
    
    # Check for after-hours anomaly
    if hour < NORMAL_START_HOUR or hour > NORMAL_END_HOUR:
        print(f"  [!] BEHAVIORAL ANOMALY DETECTED!")
        print(f"      User '{log_entry['user']}' authenticated outside standard hours.")
        print(f"      Source IP: {log_entry['source_ip']} | Hour: {hour}:00")
        print(f"      Action: Escalated for User Entity Behavior Analytics (UEBA) review.\n")
    else:
        print(f"  [-] Normal baseline behavior observed.\n")

def run_anomaly_detection():
    print("[*] Initializing Behavioral Baseline & Anomaly Engine...\n")
    for log in AUTH_LOGS:
        analyze_behavior(log)

if __name__ == "__main__":
    run_anomaly_detection()
