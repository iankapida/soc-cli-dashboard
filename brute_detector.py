# brute_detector.py
from collections import defaultdict

def detect_brute_force(filepath, threshold=2):
    print(f"[*] Analyzing authentication logs for brute-force patterns in: {filepath}\n")
    
    # Dictionary to track failed attempts per IP: {ip_address: count}
    failed_attempts = defaultdict(int)
    
    with open(filepath, "r") as f:
        for line in f:
            # Look for authentication failures
            if "Failed password" in line or "Unauthorized access" in line:
                parts = line.strip().split()
                if parts:
                    source_ip = parts[-1]
                    failed_attempts[source_ip] += 1

    print("[-] Threat Analysis Results:")
    alert_triggered = False
    
    for ip, count in failed_attempts.items():
        print(f"    [*] IP: {ip} | Failed Attempts: {count}")
        if count >= threshold:
            alert_triggered = True
            print(f"    [!] HIGH SEVERITY ALERT: Brute-force attack detected from {ip}! Total failures: {count}")
            
    if not alert_triggered:
        print("    [+] Status: No threshold violations detected.")

if __name__ == "__main__":
    log_path = "suspect_traffic.log"
    detect_brute_force(log_path, threshold=2)
