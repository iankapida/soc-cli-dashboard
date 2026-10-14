# traffic_generator.py
import random
from datetime import datetime

def inject_test_traffic(target_log="suspect_traffic.log"):
    print("[*] Generating simulated attack traffic...")
    
    attacker_ips = ["192.168.1.50", "203.0.113.42", "198.51.100.15", "10.0.0.99"]
    actions = [
        "Failed password for root from",
        "Unauthorized access attempt by",
        "Port scan detected targeting port",
        "SQL injection payload received from"
    ]
    
    simulated_ip = random.choice(attacker_ips)
    simulated_action = random.choice(actions)
    timestamp = datetime.now().strftime('%b %d %H:%M:%S')
    
    log_entry = f"{timestamp} soc-server sshd[8241]: {simulated_action} {simulated_ip}\n"
    
    with open(target_log, "a") as f:
        f.write(log_entry)
        
    print(f"    [+] Injected log line into {target_log}:")
    print(f"        {log_entry.strip()}")

if __name__ == "__main__":
    inject_test_traffic()
