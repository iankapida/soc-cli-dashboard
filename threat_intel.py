import requests

def check_ip_reputation(ip_address, api_key=None):
    """
    Checks IP reputation against AbuseIPDB (or returns simulated metrics if no API key is set).
    """
    if not api_key:
        # Fallback simulation for local/Termux testing
        is_malicious = ip_address.startswith("185.") or ip_address.startswith("10.")
        return {
            "ip": ip_address,
            "abuse_score": 85 if is_malicious else 0,
            "status": "SUSPICIOUS" if is_malicious else "CLEAN"
        }

    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {"Accept": "application/json", "Key": api_key}
    params = {"ipAddress": ip_address, "maxAgeInDays": "90"}

    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)
        if response.status_code == 200:
            data = response.json().get("data", {})
            score = data.get("abuseConfidenceScore", 0)
            return {
                "ip": ip_address,
                "abuse_score": score,
                "status": "SUSPICIOUS" if score > 20 else "CLEAN"
            }
    except requests.RequestException as e:
        return {"ip": ip_address, "error": str(e), "status": "UNKNOWN"}

if __name__ == "__main__":
    test_ip = "185.220.101.5"
    print(f"Running threat intel check for {test_ip}...")
    print(check_ip_reputation(test_ip))
