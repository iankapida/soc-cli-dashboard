import sqlite3
import datetime

DB_FILE = "soc_incidents.db"

def fetch_unmitigated_threats():
    """Fetch high-severity threats from the database for automated containment."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, source_ip, failure_count FROM incidents WHERE severity = 'HIGH'")
    threats = cursor.fetchall()
    conn.close()
    return threats

def generate_firewall_rule(ip_address):
    """Generate a standard Linux iptables firewall block command."""
    # Real-world SOC automation tools execute or queue commands like this on edge firewalls
    rule = f"iptables -A INPUT -s {ip_address} -j DROP"
    return rule

def run_remediation():
    print("[*] Initializing Automated Incident Remediation Pipeline...\n")
    threats = fetch_unmitigated_threats()
    
    if not threats:
        print("[-] No high-severity threats require containment.")
        return

    for threat in threats:
        inc_id, ip, failures = threat
        firewall_command = generate_firewall_rule(ip)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("=" * 60)
        print(f"[!] CONTAINMENT ACTION TRIGGERED FOR INCIDENT #{inc_id}")
        print("=" * 60)
        print(f"  Target IP     : {ip}")
        print(f"  Trigger Cause : {failures} brute-force attempts")
        print(f"  Action Taken  : Generated Network Containment Rule")
        print(f"  Command Draft : {firewall_command}")
        print(f"  Timestamp     : {timestamp}")
        print("  Status        : SUCCESS (Rule ready for deployment)")
        print("=" * 60 + "\n")

if __name__ == "__main__":
    run_remediation()
