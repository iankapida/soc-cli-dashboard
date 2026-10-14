# Simulated network flow records (Source IP, Destination IP, Port, Bytes Transferred)
NETWORK_FLOWS = [
    {"src": "192.168.1.15", "dst": "10.0.0.1", "port": 443, "bytes": 25400},
    {"src": "192.168.1.22", "dst": "10.0.0.1", "port": 80, "bytes": 12000},
    # Suspicious massive data exfiltration to an unknown external IP
    {"src": "192.168.1.50", "dst": "203.0.113.250", "port": 4444, "bytes": 8500000},
    {"src": "192.168.1.10", "dst": "10.0.0.2", "port": 53, "bytes": 450}
]

# Threshold for suspicious outbound byte transfer (e.g., > 1 MB)
BYTE_THRESHOLD = 1000000

def analyze_network_flows():
    print("[*] Initializing Network Flow & Traffic Anomaly Analyzer...\n")
    anomalies = 0
    
    for flow in NETWORK_FLOWS:
        src = flow["src"]
        dst = flow["dst"]
        port = flow["port"]
        bytes_transferred = flow["bytes"]
        
        print(f"[*] Flow: {src} -> {dst} | Port: {port} | Volume: {bytes_transferred:,} bytes")
        
        if bytes_transferred > BYTE_THRESHOLD or port == 4444:
            anomalies += 1
            print(f"  [!] NETWORK SECURITY ALERT: High-volume or suspicious port communication detected!")
            print(f"      Potential data exfiltration or unauthorized tunnel in progress.\n")
        else:
            print(f"  [-] Traffic flow normal. Within baseline parameters.\n")
            
    print("=" * 50)
    print(f"[*] Network Analysis Completed. Anomalies flagged: {anomalies}")
    print("=" * 50)

if __name__ == "__main__":
    analyze_network_flows()
