import os
import sys
import json
import argparse

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

def display_incident_report(flagged_ips, export_json=None):
    """Displays a clean security incident report and optionally exports to JSON."""
    print("\n[!] --- SECURITY INCIDENT REPORT: BRUTE-FORCE DETECTION ---")
    if not flagged_ips:
        print("[+] No brute-force activity detected above threshold.")
    else:
        print(f"{'IP ADDRESS':<20} | {'FAILED ATTEMPTS'}")
        print("-" * 38)
        for ip, count in flagged_ips:
            print(f"{ip:<20} | {count}")
    print("-" * 55 + "\n")

    if export_json:
        report_data = [{"ip": ip, "failed_attempts": count} for ip, count in flagged_ips]
        try:
            with open(export_json, 'w', encoding='utf-8') as f:
                json.dump(report_data, f, indent=4)
            print(f"[+] Incident report successfully exported to {export_json}")
        except Exception as e:
            print(f"[-] Failed to export JSON report: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SOC CLI Dashboard - Security Log Analyzer")
    parser.add_argument("--log", default="auth_sample.log", help="Path to the authentication log file")
    parser.add_argument("--threshold", type=int, default=3, help="Failed attempt threshold for brute-force detection")
    parser.add_argument("--export", help="Filename to export the incident report as JSON")
    
    args = parser.parse_args()

    print(f"[*] Analyzing log file: {args.log} (Threshold: {args.threshold})")
    failed, accepted = parse_auth_log(args.log)
    flagged = detect_brute_force(failed, threshold=args.threshold)
    display_incident_report(flagged, export_json=args.export)
