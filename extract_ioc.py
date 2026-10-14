import re

# Unstructured incident report text containing hidden IP addresses
incident_report = """
Incident flagged by firewall telemetry. 
Primary attacker address is 192.168.100.45, 
secondary relay observed at 10.0.0.99. 
Please isolate these nodes immediately.
"""

# Regular expression pattern for matching standard IPv4 addresses
ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

print("[*] Scanning incident report for Indicators of Compromise (IoCs)...")
found_ips = re.findall(ip_pattern, incident_report)

if found_ips:
    print(f"[+] Extracted IP Addresses: {found_ips}")
else:
    print("[-] No IP addresses found.")
