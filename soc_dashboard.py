#!/usr/bin/env python3
import sys

def main():
    print("==================================================")
    print("   Enterprise Security Operations Center (SOC) CLI   ")
    print("==================================================")
    print(" [1] Ultimate Master Orchestrator (8-Phase Pipeline)")
    print(" [2] Proactive Port Scanner")
    print(" [3] File Integrity Monitor (FIM)")
    print(" [4] Cloud API & JWT Token Auditor")
    print(" [5] IAM Privilege & Access Control Auditor")
    print(" [6] DFIR Forensic Artifact Parser")
    print(" [7] Network Flow Anomaly Analyzer")
    print(" [8] Endpoint Security Monitor")
    print("==================================================")
    
    choice = input("Select a security module (1-8): ")
    print(f"[*] Initializing module {choice}...")

if __name__ == "__main__":
    main()
