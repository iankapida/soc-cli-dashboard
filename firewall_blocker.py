# firewall_blocker.py
import os
from datetime import datetime

def block_ip(target_ip, blocklist_file="firewall_deny.list"):
    print(f"[*] Initiating automated containment protocol for IP: {target_ip}")
    
    # Check if blocklist exists, create if not
    if not os.path.exists(blocklist_file):
        with open(blocklist_file, "w") as f:
            f.write("# Automated SOC Firewall Deny-List\n")
            
    # Read existing blocklist to avoid duplicate entries
    with open(blocklist_file, "r") as f:
        blocked_ips = f.read()
        
    if target_ip in blocked_ips:
        print(f"    [!] Warning: IP {target_ip} is already present in the firewall deny-list.")
        return
        
    # Append new malicious IP with timestamp and audit trail
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f"{target_ip} # Blocked by SOC Automation on {timestamp}\n"
    
    with open(blocklist_file, "a") as f:
        f.write(entry)
        
    print(f"    [+] Success: IP {target_ip} successfully added to {blocklist_file}")
    print("    [+] Firewall rules reloaded. Traffic from this source will now be dropped.")

if __name__ == "__main__":
    # Automatically block the malicious IP identified in our previous investigations
    malicious_ip = "192.168.1.50"
    block_ip(malicious_ip)
