# Simulated list of discovered vulnerabilities with CVSS severity scores
vulnerabilities = [
    {"id": "CVE-2026-1001", "name": "Outdated OpenSSL Version", "score": 4.3},
    {"id": "CVE-2026-1002", "name": "Remote Code Execution (RCE)", "score": 9.8},
    {"id": "CVE-2026-1003", "name": "Missing Security Header", "score": 5.5},
    {"id": "CVE-2026-1004", "name": "Default Admin Credentials", "score": 8.9}
]

print("[*] Processing vulnerability scan results...")
for vuln in vulnerabilities:
    score = vuln["score"]
    if score >= 9.0:
        level = "CRITICAL"
    elif score >= 7.0:
        level = "HIGH"
    elif score >= 4.0:
        level = "MEDIUM"
    else:
        level = "LOW"
        
    print(f"[!] [{level}] {vuln['id']} ({vuln['name']}) - Score: {score}")
