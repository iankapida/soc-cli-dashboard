import concurrent.futures
import time

# Simulated list of critical infrastructure ports to check concurrently
target_ports = [21, 22, 23, 80, 443, 3389, 8080]

def scan_port(port):
    # Simulating network latency for socket connection checks
    time.sleep(0.3)
    # Common service mapping dictionary
    services = {21: "FTP", 22: "SSH", 23: "Telnet", 80: "HTTP", 443: "HTTPS", 3389: "RDP", 8080: "HTTP-Proxy"}
    service_name = services.get(port, "Unknown")
    
    # Simulate port states (Closed vs Open)
    is_open = port in [22, 80, 443]
    return port, service_name, is_open

print("[*] Initializing Multi-Threaded Port Scanner Engine...")
print("[*] Dispatching concurrent worker threads...")

# Utilizing ThreadPoolExecutor for high-speed parallel execution
open_ports = []
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(scan_port, target_ports)
    
    for port, service, is_open in results:
        if is_open:
            print(f"[+] [OPEN] Port {port} ({service}) detected active.")
            open_ports.append((port, service))
        else:
            print(f"[-] [CLOSED] Port {port} ({service}) filtered.")

print(f"\n[+] Scan complete. Found {len(open_ports)} active attack surface vectors.")
