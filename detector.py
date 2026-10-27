import re
from datetime import datetime, timedelta

def detect_brute_force(log_lines, threshold=3, window_seconds=10):
    failed_attempts = {}
    alerts = []

    for line in log_lines:
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

    for ip, timestamps in failed_attempts.items():
        timestamps.sort()
        for i in range(len(timestamps)):
            window_count = 1
            for j in range(i + 1, len(timestamps)):
                if (timestamps[j] - timestamps[i]) <= timedelta(seconds=window_seconds):
                    window_count += 1
            if window_count >= threshold:
                alerts.append(f"[CRITICAL] Potential Brute-Force Attack detected from IP: {ip} ({window_count} failures)")
                break

    return alerts

# Test execution block so it prints results when run directly
if __name__ == "__main__":
    sample_logs = [
        "Oct 27 08:12:01 server sshd[4521]: Failed password for invalid user admin from 192.168.1.50 port 54122 ssh2",
        "Oct 27 08:12:03 server sshd[4523]: Failed password for invalid user admin from 192.168.1.50 port 54124 ssh2",
        "Oct 27 08:12:05 server sshd[4525]: Failed password for invalid user admin from 192.168.1.50 port 54126 ssh2"
    ]
    
    print("[*] Testing Brute-Force Detection Logic...")
    detected_alerts = detect_brute_force(sample_logs)
    for alert in detected_alerts:
        print(alert)
