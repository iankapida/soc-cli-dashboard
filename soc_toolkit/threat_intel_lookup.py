import urllib.request
import json
import sqlite3

DB_FILE = "soc_incidents.db"

def fetch_high_severity_ips():
    """Retrieve HIGH severity IPs from our local SQLite database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT source_ip FROM incidents WHERE severity = 'HIGH'")
    ips = [row[0] for row in cursor.fetchall()]
    conn.close()
    return ips

def query_threat_intel(ip_address):
    """
    Simulate a Threat Intelligence API lookup (e.g., AbuseIPDB or custom intel feed).
    In a live environment, you would insert your API key and endpoint URL here.
    """
    print(f"[*] Querying Threat Intelligence API for IP: {ip_address}...")
    
    # For demonstration, we'll use a public test API or simulate a structured response
    # Real-world analysts use requests/urllib with headers like {'Key': 'YOUR_API_KEY'}
    
    # Simulating API response payload based on real threat feed structures
    if ip_address == "203.0.113.88":
        mock_response = {
            "ipAddress": ip_address,
            "isPublic": True,
            "abuseConfidenceScore": 95,
            "country": "XX",
            "usageType": "Data Center/WebHosting/Transit",
            "totalReports": 142
        }
        return mock_response
    else:
        return {"ipAddress": ip_address, "abuseConfidenceScore": 0, "totalReports": 0}

def run_enrichment():
    print("[*] Initializing Threat Intelligence Enrichment Pipeline...\n")
    target_ips = fetch_high_severity_ips()
    
    if not target_ips:
        print("[-] No high-severity IPs found in database to enrich.")
        return

    for ip in target_ips:
        intel_data = query_threat_intel(ip)
        
        print("\n" + "=" * 50)
        print(f"THREAT INTEL REPORT FOR: {intel_data['ipAddress']}")
        print("=" * 50)
        print(f"  Abuse Score : {intel_data['abuseConfidenceScore']}% malicious")
        print(f"  Total Reports: {intel_data['totalReports']} global reports")
        print(f"  Network Type : {intel_data.get('usageType', 'Unknown')}")
        
        if intel_data['abuseConfidenceScore'] > 80:
            print("  [!] VERDICT: Highly Malicious. Permanent block enforced.")
        else:
            print("  [-] VERDICT: Low risk / Monitor.")
        print("=" * 50 + "\n")

if __name__ == "__main__":
    run_enrichment()
