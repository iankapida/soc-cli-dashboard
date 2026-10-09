# Simulated metrics for your portable cybersecurity toolkit lab
metrics = {
    "ports_scanned": 5,
    "failed_logins_detected": 3,
    "iocs_extracted": 2,
    "firewall_rules_enforced": 4,
    "vulnerabilities_triaged": 4
}

print("========================================")
print("     PORTABLE SOC SECURITY DASHBOARD    ")
print("========================================")
for category, count in metrics.items():
    formatted_name = category.replace("_", " ").title()
    print(f"[*] {formatted_name}: {count}")
print("========================================")
print("[+] Status: Lab telemetry stable. All systems monitored.")
