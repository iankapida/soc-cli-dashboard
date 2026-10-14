import socket
import concurrent.futures
import time

TARGET_HOST = "127.0.0.1"
# Common ports checked in security audits (SSH, HTTP, FTP, MySQL, etc.)
COMMON_PORTS = [21, 22, 80, 443, 3306, 8080]

def scan_port(port):
    """Attempt a TCP socket connection to determine if a port is open."""
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        
        # Try connecting to the target host and port
        result = s.connect_ex((TARGET_HOST, port))
        s.close()
        
        if result == 0:
            return port, "OPEN"
        else:
            return port, "CLOSED"
    except Exception as e:
        return port, f"ERROR: {e}"

def run_port_scanner():
    print(f"[*] Initializing Proactive Port Scanner against {TARGET_HOST}...\n")
    start_time = time.time()
    
    # Use multi-threading to scan multiple ports concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(scan_port, COMMON_PORTS)
        
    print("=" * 50)
    print(f"PORT SCAN RESULTS FOR: {TARGET_HOST}")
    print("=" * 50)
    for port, status in results:
        marker = "[+]" if status == "OPEN" else "[-]"
        print(f"  {marker} Port {port:<5} : {status}")
        
    elapsed = round(time.time() - start_time, 2)
    print("=" * 50)
    print(f"[*] Scan completed in {elapsed} seconds.")

if __name__ == "__main__":
    run_port_scanner()
