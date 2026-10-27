import sys
from detector import detect_brute_force
from enrichment import enrich_ip
from sniffer import demonstrate_packet_parsing

def main():
    print("==================================================")
    print("     SOC CLI DASHBOARD - AUTOMATED PIPELINE       ")
    print("==================================================")
    
    print("\n[+] Step 1: Running Log Analysis & Threat Correlation...")
    alerts, iocs = detect_brute_force("auth.log")
    for alert in alerts:
        print(f"  {alert}")
        
    print("\n[+] Step 2: Running Threat Intelligence Enrichment...")
    target_ips = iocs.get("source_ips", ["192.168.1.50"])
    for ip in target_ips:
        intel = enrich_ip(ip)
        print(f"  -> IP: {ip} | Reputation: {intel['reputation']} | Confidence: {intel['confidence_score']}%")
        
    print("\n[+] Step 3: Running Network Packet Dissection Parser...")
    demonstrate_packet_parsing()
    
    print("\n==================================================")
    print("[*] Full SOC Pipeline Execution Completed.")

if __name__ == "__main__":
    main()
