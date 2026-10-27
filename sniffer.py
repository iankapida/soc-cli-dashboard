from scapy.all import IP, TCP, UDP, Ether

def demonstrate_packet_parsing():
    print("[*] Initializing offline Scapy packet parser...")
    
    # Construct a synthetic packet in memory (bypasses Android raw socket restrictions)
    synthetic_packet = Ether() / IP(src="192.168.1.50", dst="10.0.0.1") / TCP(sport=54128, dport=22, flags="S")
    
    print("\n--- PACKET INSPECTION & DISSECTION ---")
    print(f"Packet Summary: {synthetic_packet.summary()}")
    
    # Extract IP layer attributes
    if IP in synthetic_packet:
        print(f"Source IP: {synthetic_packet[IP].src}")
        print(f"Destination IP: {synthetic_packet[IP].dst}")
        
    # Extract TCP layer attributes & flags
    if TCP in synthetic_packet:
        print(f"Source Port: {synthetic_packet[TCP].sport}")
        print(f"Destination Port: {synthetic_packet[TCP].dport}")
        print(f"TCP Flags: {synthetic_packet[TCP].flags}")

if __name__ == "__main__":
    demonstrate_packet_parsing()
