import re
import subprocess
import json
from datetime import datetime, timedelta

def contain_threat(ip_address, simulate=True):
    cmd = f"iptables -A INPUT -s {ip_address} -j DROP"
    if simulate:
        return f"[CONTAINMENT ACTION (SIMULATED)] Executed: {cmd}"
    else:
        try:
            subprocess.run(cmd.split(), check=True)
            return f"[CONTAINMENT ACTION (SUCCESS)] IP {ip_address} successfully blocked."
        except subprocess.CalledProcessError as e:
            return f"[-] Containment failed: {e}"

def export_incident_report(alerts, iocs, filename="incident_report.json"):
    """
    Export IoCs and alerts to a structured JSON file for ticketing/forensics.
    """
    report = {
        "timestamp": datetime.now().isoformat(),
        "indicators_of_compromise": iocs,
        "generated_alerts": alerts
    }
    with open(filename, 'w') as f:
        json.dump(report, f, indent=4)
    return f"[FORENSICS] Incident report exported successfully to {filename}"

def detect_brute_force(file_path, threshold=3, window_seconds=10):
    failed_attempts = {}
    alerts = []
    iocs = {"source_ips": [], "compromised_accounts": [], "persistence_mechanisms": []}

    try:
        with open(file_path, 'r') as file:
            log_lines = file.readlines()
    except FileNotFoundError:
        print(f"[-] Error: Log file '{file_path}' not found.")
        return [], {}

    for line in log_lines:
        # 1. Track failed authentication attempts
        if "Failed password" in line:
            match_ip = re.search(r'from\s+([0-9.]+)', line)
            match_time = re.search(r'([A-Za-z]+\s+\d+\s+\d{2}:\d{2}:\d{2})', line)
            
            if match_ip and match_time:
                ip = match_ip.group(1)
                timestamp_str = match_time.group(1)
                dt = datetime.strptime(f"2026 {timestamp_str}", "%Y %b %d %H:%M:%S")
                
                if ip not in failed_attempts:
                    failed_attempts[ip] = []
                failed_attempts[ip].append(dt)
                if ip not in iocs["source_ips"]:
                    iocs["source_ips"].append(ip)

        # 2. Check for credential compromise (successful login post-brute force)
        elif "Accepted password" in line:
            match_ip = re.search(r'from\s+([0-9.]+)', line)
            match_user = re.search(r'for\s+(\S+)', line)
            if match_ip and match_user:
                ip = match_ip.group(1)
                user = match_user.group(1)
                if ip in failed_attempts and len(failed_attempts[ip]) >= threshold:
                    alerts.append(f"[CRITICAL] COMPROMISE ALERT: Successful login for '{user}' from IP {ip} immediately following a brute-force attack!")
                    if user not in iocs["compromised_accounts"]:
                        iocs["compromised_accounts"].append(user)
                    
                    containment_msg = contain_threat(ip, simulate=True)
                    alerts.append(containment_msg)

        # 3. Check for Persistence Indicators (e.g., new user creation or key additions)
        elif "new user" in line or "useradd" in line:
            alerts.append(f"[HIGH] PERSISTENCE ALERT: Potential backdoor user account created.")
            iocs["persistence_mechanisms"].append(line.strip())

    # Check sliding window thresholds for raw brute-force spikes
    for ip, timestamps in failed_attempts.items():
        timestamps.sort()
        for i in range(len(timestamps)):
            window_count = 1
            for j in range(i + 1, len(timestamps)):
                if (timestamps[j] - timestamps[i]) <= timedelta(seconds=window_seconds):
                    window_count += 1
            if window_count >= threshold:
                alerts.append(f"[WARNING] Potential Brute-Force Attack detected from IP: {ip} ({window_count} failures)")
                break

    return alerts, iocs

if __name__ == "__main__":
    target_log = "auth.log"
    print(f"[*] Analyzing log file: {target_log}...")
    security_alerts, extracted_iocs = detect_brute_force(target_log)
    
    print("\n--- SECURITY ALERTS GENERATED ---")
    for alert in security_alerts:
        print(alert)
        
    print("\n--- GENERATING INCIDENT ARTIFACTS ---")
    report_status = export_incident_report(security_alerts, extracted_iocs)
    print(report_status)
