import os
import sys

def parse_auth_log(log_path):
    """Safely parses Linux authentication logs for failed and accepted SSH attempts."""
    failed_attempts = {}
    accepted_attempts = []
    
    if not os.path.exists(log_path):
        print(f"[-] Error: Log file '{log_path}' not found.")
        return failed_attempts, accepted_attempts

    try:
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                if "Failed password" in line:
                    parts = line.split()
                    try:
                        ip_index = parts.index("from") + 1
                        if ip_index < len(parts):
                            ip = parts[ip_index]
                            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1
                    except (ValueError, IndexError):
                        continue
                elif "Accepted password" in line:
                    accepted_attempts.append(line.strip())
                    
    except Exception as e:
        print(f"[-] An error occurred while reading the log: {e}")
        
    return failed_attempts, accepted_attempts

def detect_brute_force(failed_attempts, threshold=3):
    """Flags IP addresses that exceed the specified failure threshold."""
    flagged_ips = {}
    for ip, count in failed_attempts.items():
        if count >= threshold:
            flagged_ips[ip] = count
            
    sorted_flagged = sorted(flagged_ips.items(), key=lambda x: x[1], reverse=True)
    return sorted_flagged

def display_incident_report(flagged_ips):
    """Displays a clean security incident report in the terminal."""
    print("\n[!] --- SECURITY INCIDENT REPORT: BRUTE-FORCE DETECTION ---")
    if not flagged_ips:
        print("[+] No brute-force activity detected above threshold.")
    else:
        print(f"{'IP ADDRESS':<20} | {'FAILED ATTEMPTS'}")
        print("-" * 38)
        for ip, count in flagged_ips:
            print(f"{ip:<20} | {count}")
    print("-" * 55 + "\n")

if __name__ == "__main__":
    log_file = "auth_sample.log"
    print(f"[*] Analyzing log file: {log_file}")
    failed, accepted = parse_auth_log(log_file)
    flagged = detect_brute_force(failed, threshold=3)
    display_incident_report(flagged)
