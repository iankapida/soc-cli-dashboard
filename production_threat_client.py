import json
import os
import requests

def query_threat_intel(indicator):
    # Professional standard: Load API keys from environment variables instead of hardcoding
    api_key = os.getenv("THREAT_INTEL_API_KEY", "mock_secure_token_12345")
    api_endpoint = f"https://api.mockthreatintel.com/v3/indicators/{indicator}"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
        "User-Agent": "SOC-Automation-Client/1.0"
    }
    
    try:
        print(f"[*] Querying threat intelligence provider for: {indicator}")
        # In a live environment, use requests.get with a timeout to prevent hanging threads
        # response = requests.get(api_endpoint, headers=headers, timeout=5)
        
        # Simulating a production HTTP response object for your local lab
        class MockResponse:
            status_code = 200
            def json(self):
                return {
                    "indicator": indicator,
                    "reputation": "malicious",
                    "threat_score": 88,
                    "mitre_technique": "T1110 - Brute Force",
                    "recommendation": "Isolate host and revoke session tokens."
                }
        
        response = MockResponse()
        
        # Professional HTTP status code validation
        if response.status_code == 200:
            data = response.json()
            print(f"[+] Success: Retrieved telemetry for {data['indicator']}")
            print(f"    - Threat Score: {data['threat_score']}/100")
            print(f"    - Associated TTP: {data['mitre_technique']}")
            print(f"    - Playbook Action: {data['recommendation']}")
        elif response.status_code == 429:
            print("[!] Warning: API rate limit exceeded. Backing off and retrying...")
        else:
            print(f"[-] Error: Received unexpected HTTP status code {response.status_code}")
            
    except requests.exceptions.Timeout:
        print("[-] Error: Connection timed out while reaching the threat intelligence feed.")
    except requests.exceptions.RequestException as e:
        print(f"[-] Critical Network Error: {e}")
    except json.JSONDecodeError:
        print("[-] Error: Failed to parse incoming JSON payload from API response.")

# Execute the production client logic
query_threat_intel("192.168.100.45")
