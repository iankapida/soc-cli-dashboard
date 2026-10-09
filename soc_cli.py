import sqlite3
import sys

def init_db():
    conn = sqlite3.connect("soc_incidents.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_ip TEXT,
            failure_count INTEGER,
            severity TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def display_menu():
    print("==========================================================")
    print("   ENTERPRISE SECURITY OPERATIONS CENTER (SOC) - CLI DASHBOARD")
    print("==========================================================")
    print("[1] Run Ultimate Master Orchestrator (Full 8-Phase Pipeline)")
    print("[2] Run Proactive Port Scanner")
    print("[3] Run File Integrity Monitor (FIM)")
    print("[4] Run Cloud API & JWT Token Auditor")
    print("[5] Run IAM Privilege & Access Control Auditor")
    print("[6] Run DFIR Forensic Artifact Parser")
    print("[7] Run Network Flow Anomaly Analyzer")
    print("[8] Run Endpoint Security Monitor")
    print("[9] Run Threat Intelligence IP Checker")
    print("[10] Run Enterprise SIEM Query & Threshold Engine")
    print("[0] Exit Toolkit")
    print("==========================================================")

def run_siem_engine():
    print("\n[*] Running Enterprise SIEM Query & Threshold Engine...")
    conn = sqlite3.connect("soc_incidents.db")
    cursor = conn.cursor()
    
    # Example query flagging IPs where failure_count > 3
    cursor.execute("SELECT source_ip, failure_count, severity, timestamp FROM incidents WHERE failure_count > 3")
    results = cursor.fetchall()
    
    if not results:
        print("[+] No high-risk threshold breaches detected (failure_count > 3).")
    else:
        print(f"[!] ALERT: Found {len(results)} high-risk threshold violation(s):")
        for row in results:
            print(f"    -> IP: {row[0]} | Failures: {row[1]} | Severity: {row[2]} | Time: {row[3]}")
    conn.close()

def main():
    init_db()
    while True:
        display_menu()
        choice = input("[?] Select an operational module (0-10): ").strip()
        
        if choice == '1':
            print("\n[*] Executing Ultimate Master Orchestrator...")
        elif choice == '2':
            print("\n[*] Executing Proactive Port Scanner...")
        elif choice == '3':
            print("\n[*] Executing File Integrity Monitor...")
        elif choice == '4':
            print("\n[*] Executing Cloud API & JWT Token Auditor...")
        elif choice == '5':
            print("\n[*] Executing IAM Privilege & Access Control Auditor...")
        elif choice == '6':
            print("\n[*] Executing DFIR Forensic Artifact Parser...")
        elif choice == '7':
            print("\n[*] Executing Network Flow Anomaly Analyzer...")
        elif choice == '8':
            print("\n[*] Executing Endpoint Security Monitor...")
        elif choice == '9':
            print("\n[*] Executing Threat Intelligence IP Checker...")
        elif choice == '10':
            run_siem_engine()
        elif choice == '0':
            print("\n[+] Exiting SOC Toolkit. Stay secure!")
            sys.exit(0)
        else:
            print("\n[-] Invalid selection. Please choose a valid option (0-10).")
        
        input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    main()
