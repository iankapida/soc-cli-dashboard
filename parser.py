import sys
import re

def parse_logs(filepath):
    success_count = 0
    fail_count = 0
    ip_failures = {}

    try:
        with open(filepath, 'r') as file:
            for line in file:
                if "Accepted password" in line:
                    success_count += 1
                elif "Failed password" in line:
                    fail_count += 1
                    match = re.search(r'from\s+([0-9.]+)', line)
                    if match:
                        ip = match.group(1)
                        ip_failures[ip] = ip_failures.get(ip, 0) + 1

        print(f"[+] Analyzing Log File: {filepath}")
        print("-" * 50)
        print(f"Total Events Processed : {success_count + fail_count}")
        print(f"Successful Logins     : {success_count}")
        print(f"Failed Login Attempts : {fail_count}\n")

        if ip_failures:
            print("[!] SUSPICIOUS ACTIVITY DETECTED:")
            for ip, count in ip_failures.items():
                if count >= 3:
                    print(f"- IP: {ip} | Failed Attempts: {count} (Possible Brute-Force)")
        print("-" * 50)

    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
        sys.exit(2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parser.py <logfile>")
        sys.exit(1)
    parse_logs(sys.argv[1])
