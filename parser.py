# parser.py
def parse_security_logs(filepath):
    unique_iocs = set()
    
    print(f"[*] Scanning log file: {filepath}\n")
    
    with open(filepath, "r") as file:
        for line in file:
            # Equivalent to: grep "ALERT"
            if "ALERT" in line:
                # Equivalent to: awk '{print $NF}' and uniq/sort (via set)
                parts = line.strip().split()
                if parts:
                    attacker_ip = parts[-1]
                    unique_iocs.add(attacker_ip)
                    
    return unique_iocs

if __name__ == "__main__":
    log_path = "suspect_traffic.log"
    iocs = parse_security_logs(log_path)
    
    print("[-] Extracted Indicators of Compromise (IOCs):")
    for ip in iocs:
        print(f"    [!] Malicious IP: {ip}")
