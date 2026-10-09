# Simulated firewall Access Control List (ACL)
blocked_ips = ["192.168.100.45", "10.0.0.99", "203.0.113.50"]

incoming_traffic = [
    "192.168.1.10",
    "192.168.100.45",
    "172.16.0.5",
    "10.0.0.99"
]

print("[*] Evaluating incoming traffic against firewall security policy...")
for ip in incoming_traffic:
    if ip in blocked_ips:
        print(f"[X] DROP: Traffic from {ip} blocked by security policy.")
    else:
        print(f"[✓] ALLOW: Traffic from {ip} permitted.")
