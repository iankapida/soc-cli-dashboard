import re
from collections import Counter

# Define configuration parameters
LOG_SOURCE = "raw_auth_events.log"
BRUTE_FORCE_THRESHOLD = 3  # Alert if a single IP fails 3 or more times

def run_triage():
    print(f"[*] Starting automated log ingestion from {LOG_SOURCE}...")
    
    # Regular expression to extract IPv4 addresses following the word 'from'
    ip_pattern = r'from\s+(\d{1,3}(?:\.\d{1,3}){3})'
    failed_attempts = []

    try:
        with open(LOG_SOURCE, 'r') as file:
            logs = file.readlines()
    except FileNotFoundError:
        print(f"[!] Error: Log file {LOG_SOURCE} could not be found.")
        return

    # Ingestion and parsing loop (Triage Phase)
    for line in logs:
        if "FAILED" in line:
            match = re.search(ip_pattern, line)
            if match:
                attacker_ip = match.group(1)
                failed_attempts.append(attacker_ip)

    # Correlation Phase: Count occurrences to detect threshold breaches
    ip_counts = Counter(failed_attempts)

    print("\n[+] Triage Complete. Generating Security Advisory Report:\n")
    print("-" * 60)

    if not ip_counts:
        print("[-] No failed authentication anomalies detected.")
    
    for ip, count in ip_counts.items():
        if count >= BRUTE_FORCE_THRESHOLD:
            print(f"[!] HIGH SEVERITY ALERT: Brute-Force Attack Detected!")
            print(f"    Source IP : {ip}")
            print(f"    Failures  : {count} attempts")
            print(f"    Action    : Recommended immediate firewall block.")
        else:
            print(f"[-] LOW SEVERITY NOTICE: Isolated failure from {ip} ({count} attempt)")
        print("-" * 60)

if __name__ == "__main__":
    run_triage() 
   
