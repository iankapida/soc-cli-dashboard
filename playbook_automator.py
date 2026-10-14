# Simulated automated incident response playbook
incident_type = "Brute-Force Attack Detected"

print(f"[*] Triggering Automated Response Playbook for: {incident_type}")

playbook_steps = [
    "1. Isolate the affected host from the network segment.",
    "2. Capture system logs and memory dumps for forensics.",
    "3. Revoke active user sessions and force password resets.",
    "4. Push updated block rules to the perimeter firewall."
]

for step in playbook_steps:
    print(f"[x] Executing: {step}")
    
print("[+] Incident Response Playbook completed successfully. SOC ticket updated.")
