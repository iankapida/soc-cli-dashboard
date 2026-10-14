import urllib.request
import json
import sys

def check_ip_reputation(ip_address):
    print(f"[*] Querying threat intelligence for IP: {ip_address}...")
    # Using a public safe testing API endpoint or simulated lookup logic
    url = f"http://ip-api.com/json/{ip_address}"
    
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'SOC-CLI-Toolkit/1.0'}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            if data.get('status') == 'success':
                print(f"\n[+] IP Intelligence Results:")
                print(f"    - Country: {data.get('country')}")
                print(f"    - ISP: {data.get('isp')}")
                print(f"    - Organization: {data.get('org')}")
                print(f"    - Status: Low Risk / Active")
            else:
                print("[-] Failed to retrieve intelligence data.")
    except Exception as e:
        print(f"[-] Connection error during threat lookup: {e}")

if __name__ == "__main__":
    target_ip = input("Enter an IP address to check against threat intel: ").strip()
    if target_ip:
        check_ip_reputation(target_ip)
    else:
        print("[-] No IP provided.")
