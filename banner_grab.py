import requests

print("[*] Inspecting service response headers...")
try:
    response = requests.get("https://httpbin.org/headers")
    if response.status_code == 200:
        print("[+] Headers retrieved successfully:")
        for header, value in response.headers.items():
            print(f"    - {header}: {value}")
except Exception as e:
    print(f"[!] Error: {e}")
