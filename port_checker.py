import socket

# Target IP (127.0.0.1 is your device's local loopback address)
target = "127.0.0.1"
ports_to_check = [21, 22, 80, 443, 8080]

print(f"[*] Scanning network ports on {target}...")

for port in ports_to_check:
    # Create a TCP socket connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    
    # Try connecting to the port
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"[+] Port {port}: OPEN")
    else:
        print(f"[-] Port {port}: Closed")
        
    s.close()
