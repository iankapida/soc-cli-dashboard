import time
import random

def query_with_retry(indicator, max_retries=3):
    attempt = 0
    backoff_factor = 2  # Exponential growth multiplier (2s, 4s, 8s...)
    
    print(f"[*] Initializing resilient API query for indicator: {indicator}")
    
    while attempt < max_retries:
        attempt += 1
        print(f"    -> Attempt {attempt} of {max_retries} connecting to threat intelligence feed...")
        
        # Simulating API behavior: simulating a rate-limit (429) on early attempts
        # In production, check response.status_code == 429
        simulated_status_code = 429 if attempt < 3 else 200
        
        if simulated_status_code == 200:
            print(f"[+] Success: Threat intelligence payload received on attempt {attempt}.")
            return {"indicator": indicator, "status": "Clean", "reputation_score": 12}
        elif simulated_status_code == 429:
            sleep_time = backoff_factor ** attempt + random.uniform(0, 1)
            print(f"[!] Warning: HTTP 429 Rate Limit Exceeded. Backing off for {sleep_time:.2f} seconds...")
            time.sleep(sleep_time)
        else:
            print(f"[-] Error: Unexpected HTTP status {simulated_status_code}")
            break
            
    print("[-] Critical Error: Max retries reached. API query failed.")
    return None

# Execute the resilient pipeline
result = query_with_retry("10.0.0.99")
if result:
    print(f"[+] Final Parsed Result: {result}")
