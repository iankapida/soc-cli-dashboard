# packet_analyzer.py
import json

def analyze_packet_stream():
    print("[*] Initializing Scapy-style network packet dissection...")
    
    # Simulate captured network frames for analysis
    mock_packets = [
        {"src_ip": "192.168.1.50", "dst_ip": "10.0.0.1", "proto": "TCP", "dport": 22, "flags": "S", "payload_len": 0},
        {"src_ip": "203.0.113.42", "dst_ip": "10.0.0.1", "proto": "TCP", "dport": 80, "flags": "PA", "payload_len": 512},
        {"src_ip": "198.51.100.15", "dst_ip": "10.0.0.1", "proto": "UDP", "dport": 53, "flags": "NONE", "payload_len": 64}
    ]
    
    anomalies = []
    for pkt in mock_packets:
        # Flag SYN packets targeting SSH (port 22) as potential port scans / brute-force probes
        if pkt["dport"] == 22 and pkt["flags"] == "S":
            anomalies.append({
                "alert": "Potential SSH Reconnaissance / SYN Scan",
                "source": pkt["src_ip"]
            })
            
    print("-" * 50)
    print(" >>> PACKET INSPECTION COMPLETE <<<")
    print(f" Total Packets Analyzed : {len(mock_packets)}")
    print(f" Anomalies Flagged      : {len(anomalies)}")
    print(json.dumps(anomalies, indent=4))
    print("-" * 50)

if __name__ == "__main__":
    analyze_packet_stream()
