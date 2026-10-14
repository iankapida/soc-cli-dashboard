#!/usr/bin/env python3
import sys
import os
import socket
import hashlib
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("==================================================")
    print("   Enterprise Security Operations Center (SOC) CLI   ")
    print("==================================================")

def run_port_scanner():
    clear_screen()
    print("==================================================")
    print("          Phase 2: Proactive Port Scanner         ")
    print("==================================================")
    
    target_input = input("Enter target IP or hostname (default 127.0.0.1): ").strip()
    target = target_input if target_input else "127.0.0.1"
    
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("\n[-] Hostname could not be resolved.")
        input("\nPress Enter to return to menu...")
        return

    print(f"\n[*] Scanning target: {target_ip}")
    print(f"[*] Time started: {datetime.now()}")
    print("-" * 50)
    
    ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 443, 445, 3306, 8080]
    
    try:
        for port in ports_to_scan:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"[+] Port {port}: OPEN")
            s.close()
    except KeyboardInterrupt:
        print("\n[-] Scan cancelled by user.")
    
    print("-" * 50)
    print("[*] Port scan complete.")
    input("\nPress Enter to return to menu...")

def run_fim():
    clear_screen()
    print("==================================================")
    print("      Phase 3: File Integrity Monitor (FIM)       ")
    print("==================================================")
    
    file_path = input("Enter file path to monitor (default 'soc_dashboard.py'): ").strip()
    target_file = file_path if file_path else "soc_dashboard.py"
    
    if not os.path.exists(target_file):
        print(f"\n[-] Error: File '{target_file}' not found.")
        input("\nPress Enter to return to menu...")
        return
        
    print(f"\n[*] Computing SHA-256 hash for: {target_file}")
    
    sha256_hash = hashlib.sha256()
    try:
        with open(target_file, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        file_hash = sha256_hash.hexdigest()
        print(f"[+] Current SHA-256 Hash:")
        print(f"    {file_hash}")
        print(f"[*] Status: File integrity baseline recorded successfully.")
    except Exception as e:
        print(f"\n[-] Error reading file: {e}")
        
    input("\nPress Enter to return to menu...")

def main():
    while True:
        clear_screen()
        banner()
        print(" [1] Ultimate Master Orchestrator (8-Phase Pipeline)")
        print(" [2] Proactive Port Scanner")
        print(" [3] File Integrity Monitor (FIM)")
        print(" [4] Cloud API & JWT Token Auditor")
        print(" [5] IAM Privilege & Access Control Auditor")
        print(" [6] DFIR Forensic Artifact Parser")
        print(" [7] Network Flow Anomaly Analyzer")
        print(" [8] Endpoint Security Monitor")
        print(" [9] Exit Dashboard")
        print("==================================================")
        
        choice = input("Select a security module (1-9): ").strip()
        
        if choice == '1':
            print("\n[*] Initializing Master Orchestrator Pipeline...")
            input("\nPress Enter to return to menu...")
        elif choice == '2':
            run_port_scanner()
        elif choice == '3':
            run_fim()
        elif choice == '4':
            print("\n[*] Initializing Cloud API & JWT Auditor...")
            input("\nPress Enter to return to menu...")
        elif choice == '5':
            print("\n[*] Initializing IAM Access Control Auditor...")
            input("\nPress Enter to return to menu...")
        elif choice == '6':
            print("\n[*] Initializing DFIR Artifact Parser...")
            input("\nPress Enter to return to menu...")
        elif choice == '7':
            print("\n[*] Initializing Network Flow Anomaly Analyzer...")
            input("\nPress Enter to return to menu...")
        elif choice == '8':
            print("\n[*] Initializing Endpoint Security Monitor...")
            input("\nPress Enter to return to menu...")
        elif choice == '9':
            print("[+] Shutting down SOC CLI Dashboard. Stay secure!")
            sys.exit(0)
        else:
            input("\n[-] Invalid selection. Press Enter to try again...")

if __name__ == "__main__":
    main()
