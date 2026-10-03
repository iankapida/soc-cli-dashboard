import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    print("=" * 65)
    print("      ENTERPRISE SECURITY OPERATIONS CENTER (SOC) - CLI DASHBOARD")
    print("=" * 65)
    print(" [1] Run Ultimate Master Orchestrator (Full 8-Phase Pipeline)")
    print(" [2] Run Proactive Port Scanner")
    print(" [3] Run File Integrity Monitor (FIM)")
    print(" [4] Run Cloud API & JWT Token Auditor")
    print(" [5] Run IAM Privilege & Access Control Auditor")
    print(" [6] Run DFIR Forensic Artifact Parser")
    print(" [7] Run Network Flow Anomaly Analyzer")
    print(" [8] Run Endpoint Security Monitor")
    print("[9] Run Threat Intelligence IP Checker")
    print("[0] exit toolkit")
    print("=" * 65)

def main_menu():
    while True:
        clear_screen()
        show_banner()
        choice = input("\n[?] Select an operational module (0-9): ").strip()
        
        if choice == '1':
            print("\n[*] Launching Master SOC Orchestrator...")
            os.system("python master_soc.py")
        elif choice == '2':
            print("\n[*] Launching Port Scanner...")
            os.system("python port_scanner.py")
        elif choice == '3':
            print("\n[*] Launching File Integrity Monitor...")
            os.system("python fim_monitor.py")
        elif choice == '4':
            print("\n[*] Launching Cloud JWT Auditor...")
            os.system("python cloud_token_auditor.py")
        elif choice == '5':
            print("\n[*] Launching IAM Privilege Auditor...")
            os.system("python iam_auditor.py")
        elif choice == '6':
            print("\n[*] Launching DFIR Forensic Parser...")
            os.system("python dfir_parser.py")
        elif choice == '7':
            print("\n[*] Launching Network Flow Analyzer...")
            os.system("python network_flow.py")
        elif choice == '8':
            print("\n[*] Launching Endpoint Security Monitor...")
            os.system("python endpoint_monitor.py")
        elif choice == '9':
            print("\n[*] Launching Threat Intelligence IP Checker...")
            os.system("python threat_intel_checker.py")
        elif choice == '0':
            print("\n[*] Exiting SOC Dashboard. Stay secure!")
            sys.exit(0)
        else:
            print("\n[!] Invalid selection. Please choose a number between 0 and 8.")
            
        input("\n[Press Enter to return to the main dashboard...]")

if __name__ == "__main__":
    main_menu()
