import requests

try:
    response = requests.get("https://api.ipify.org?format=json")
    data = response.json()
    print(f"[*] Current External IP: {data['ip']}")
except Exception as e:
    print(f"[!] Error fetching IP: {e}")
