import json

def enrich_ip(ip_address):
    """
    Simulates querying a Threat Intelligence API (e.g., AbuseIPDB / VirusTotal)
    to retrieve threat scores, tags, and actor attribution for an IoC.
    """
    # Simulated local threat database (in production, this would be an authenticated API call)
    threat_database = {
        "192.168.1.50": {
            "reputation": "Malicious",
            "confidence_score": 95,
            "threat_type": "SSH Brute-Force / Credential Access",
            "country": "Internal Subnet",
            "is_known_attacker": True
        },
        "10.0.0.15": {
            "reputation": "Suspicious",
            "confidence_score": 60,
            "threat_type": "Port Scanning",
            "country": "Internal Subnet",
            "is_known_attacker": False
        }
    }
    
    print(f"[*] Querying Threat Intelligence API for IP: {ip_address}...")
    
    if ip_address in threat_database:
        intel = threat_database[ip_address]
        return intel
    else:
        return {
            "reputation": "Unknown",
            "confidence_score": 0,
            "threat_type": "None",
            "country": "External / Public",
            "is_known_attacker": False
        }

if __name__ == "__main__":
    target_ip = "192.168.1.50"
    result = enrich_ip(target_ip)
    
    print("\n--- THREAT INTEL ENRICHMENT REPORT ---")
    print(json.dumps(result, indent=4))
