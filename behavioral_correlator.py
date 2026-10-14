import collections

event_stream = [
    {"src_ip": "192.168.100.45", "action": "LOGIN_FAIL"},
    {"src_ip": "10.0.0.99", "action": "PORT_SCAN"},
    {"src_ip": "192.168.100.45", "action": "LOGIN_FAIL"},
    {"src_ip": "192.168.100.45", "action": "SSH_BRUTE_FORCE"},
    {"src_ip": "10.0.0.99", "action": "HTTP_GET"}
]

print("[*] Initializing Behavioral Correlation Engine...")
ip_counter = collections.defaultdict(int)
threshold = 3

for event in event_stream:
    ip = event["src_ip"]
    ip_counter[ip] += 1
    print(f"[*] Processing event: IP {ip} -> Action: {event['action']}")

print("\n[*] Evaluating threshold triggers across observation window...")
for ip, count in ip_counter.items():
    if count >= threshold:
        print(f"[!] CORRELATION ALERT: IP {ip} exceeded frequency threshold with {count} correlated events.")
        print("    -> Automated Response: Escalating to incident queue and initiating containment playbook.")
    else:
        print(f"[✓] IP {ip} event volume nominal ({count} events).")
