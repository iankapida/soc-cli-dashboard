# threat_intel.py
import json

def check_ip_reputation(target_ip):
    print(f"[*] Querying Threat Intelligence feeds for IP: {target_ip}")
    
    # Simulated threat intel database (in production, this would query APIs like AbuseIPDB, VirusTotal, etc.)
    known_threats = {
        "192.168.1.50": {
            "status": "MALICIOUS",
            "threat_type": "Brute-Force / Port Scan",
            "confidence": "High",
            "country": "Unknown / Internal Range"
        },
        "10.0.0.15": {
            "status": "SUSPICIOUS",
            "threat_type": "Unauthorized Probing",
            "confidence": "Medium",
            "country": "Local Subnet"
        }
    }
    
    result = known_threats.get(target_ip, {
        "status": "CLEAN",
        "threat_type": "None",
        "confidence": "N/A",
        "country": "Unflagged"
    })
    
    print("-" * 40)
    print(f" IP Address : {target_ip}")
    print(f" Status     : {result['status']}")
    print(f" Threat Type: {result['threat_type']}")
    print(f" Confidence : {result['confidence']}")
    print("-" * 40)
    
    return result

if __name__ == "__main__":
    # Test with the attacker IP flagged in our previous logs
    suspicious_ip = "192.168.1.50"
    check_ip_reputation(suspicious_ip)
