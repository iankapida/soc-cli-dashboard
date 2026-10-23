import os
import sys
import json
import argparse

def parse_auth_log(log_path):
    """Safely parses Linux authentication logs for failed and accepted SSH attempts, extracting timestamps."""
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
                        timestamp = " ".join(parts[0:3]) if len(parts) >= 3 else "Unknown"
                        ip_index = parts.index("from") + 1
                        if ip_index < len(parts):
                            ip = parts[ip_index]
                            if ip not in failed_attempts:
                                failed_attempts[ip] = {"count": 0, "timestamps": []}
                            failed_attempts[ip]["count"] += 1
                            failed_attempts[ip]["timestamps"].append(timestamp)
                    except (ValueError, IndexError):
                        continue
                elif "Accepted password" in line:
                    accepted_attempts.append(line.strip())
                    
    except Exception as e:
        print(f"[-] An error occurred while reading the log: {e}")
        
    return failed_attempts, accepted_attempts

def detect_brute_force(failed_attempts, threshold=3):
    """Flags IP addresses, calculates severity ratings, and provides remediation recommendations."""
    flagged_ips = {}
    for ip, data in failed_attempts.items():
        count = data["count"]
        if count >= threshold:
            severity = "HIGH" if count >= 5 else "MEDIUM"
            recommendation = "Block IP via firewall (e.g., ufw/iptables) and audit target user accounts."
            
            flagged_ips[ip] = {
                "count": count,
                "timestamps": data["timestamps"],
                "severity": severity,
                "recommendation": recommendation
            }
            
    sorted_flagged = sorted(flagged_ips.items(), key=lambda x: x[1]["count"], reverse=True)
    return sorted_flagged

def display_incident_report(flagged_ips, export_json=None):
    """Displays an enhanced security incident report with timestamps and severity ratings."""
    print("\n[!] --- ENHANCED SECURITY INCIDENT REPORT: BRUTE-FORCE DETECTION ---")
    if not flagged_ips:
        print("[+] No brute-force activity detected above threshold.")
    else:
        for ip, data in flagged_ips:
            print(f"[*] Target IP      : {ip}")
            print(f"    Failed Attempts: {data['count']}")
            print(f"    Severity Level : {data['severity']}")
            print(f"    First/Last Seen: {data['timestamps'][0]} -> {data['timestamps'][-1]}")
            print(f"    Action Required: {data['recommendation']}")
            print("-" * 60)
    print("\n")

    if export_json:
        report_data = [
            {
                "ip": ip,
                "failed_attempts": data["count"],
                "severity": data["severity"],
                "timestamps": data["timestamps"],
                "recommendation": data["recommendation"]
            }
            for ip, data in flagged_ips
        ]
        try:
            with open(export_json, 'w', encoding='utf-8') as f:
                json.dump(report_data, f, indent=4)
            print(f"[+] Enhanced incident report successfully exported to {export_json}")
        except Exception as e:
            print(f"[-] Failed to export JSON report: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SOC CLI Dashboard - Enhanced Security Log Analyzer")
    parser.add_argument("--log", default="auth_sample.log", help="Path to the authentication log file")
    parser.add_argument("--threshold", type=int, default=3, help="Failed attempt threshold for brute-force detection")
    parser.add_argument("--export", help="Filename to export the incident report as JSON")
    
    args = parser.parse_args()

    print(f"[*] Analyzing log file: {args.log} (Threshold: {args.threshold})")
    failed, accepted = parse_auth_log(args.log)
    flagged = detect_brute_force(failed, threshold=args.threshold)
    display_incident_report(flagged, export_json=args.export)
