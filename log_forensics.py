# log_forensics.py
import re
import json

def forensic_log_investigation(log_file="suspect_traffic.log"):
    print(f"[*] Initiating advanced regex forensic scan on: {log_file}")
    
    # Create sample forensic log data if file is empty or missing
    sample_data = """
    Oct 15 00:40:10 soc-server sshd[9921]: Failed password for root from 192.168.1.50 port 51221 ssh2
    Oct 15 00:40:12 soc-server sshd[9921]: Failed password for root from 192.168.1.50 port 51222 ssh2
    Oct 15 00:41:00 soc-server sudo[9945]: pam_unix(sudo:session): session opened for user root by admin(uid=0)
    Oct 15 00:42:15 soc-server sshd[10020]: Accepted publickey for admin from 203.0.113.88 port 44321 ssh2
    """
    
    with open(log_file, "w") as f:
        f.write(sample_data.strip())
        
    # Regex patterns for forensic extraction
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    failed_login_pattern = r'Failed password.*from\s+([0-9\.]+)'
    
    extracted_ips = set()
    failed_attackers = []
    
    with open(log_file, "r") as f:
        for line in f:
            # Extract all IPs
            found_ips = re.findall(ip_pattern, line)
            extracted_ips.update(found_ips)
            
            # Extract specific failed login sources
            match = re.search(failed_login_pattern, line)
            if match:
                failed_attackers.append(match.group(1))
                
    forensic_results = {
        "total_unique_ips_found": list(extracted_ips),
        "brute_force_sources": failed_attackers,
        "investigation_status": "COMPLETED"
    }
    
    print("-" * 50)
    print(" >>> FORENSIC INVESTIGATION REPORT <<<")
    print(json.dumps(forensic_results, indent=4))
    print("-" * 50)

if __name__ == "__main__":
    forensic_log_investigation()
