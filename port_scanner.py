# port_scanner.py
import socket
from datetime import datetime

def scan_ports(target_host, ports):
    print(f"[*] Starting TCP Port Scan on target: {target_host}")
    print(f"[*] Time started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    for port in ports:
        try:
            # Create a socket object (IPv4, TCP)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.0) # 1 second timeout for responsiveness
            
            # Attempt connection
            result = s.connect_ex((target_host, port))
            
            if result == 0:
                print(f"    [+] Port {port}: OPEN")
            s.close()
        except socket.error:
            pass
            
    print("-" * 50)
    print("[*] Port scan complete.")

if __name__ == "__main__":
    # Scan localhost safely within your Termux environment
    target = "127.0.0.1"
    common_ports = [21, 22, 80, 443, 3306, 8080]
    scan_ports(target, common_ports)
