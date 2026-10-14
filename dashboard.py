# dashboard.py
import os
from datetime import datetime

def check_file_metadata(filepath):
    if not os.path.exists(filepath):
        return "File missing", 0, "N/A"
    
    stats = os.stat(filepath)
    size = stats.st_size
    modified_time = datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
    
    # Check permissions (octal format)
    perms = oct(stats.st_mode)[-3:]
    return perms, size, modified_time

def render_dashboard():
    target_log = "suspect_traffic.log"
    perms, size, mod_time = check_file_metadata(target_log)
    
    print("=" * 40)
    print("       SOC TERMINAL DASHBOARD       ")
    print("=" * 40)
    print(f" Target File  : {target_log}")
    print(f" Permissions  : {perms} (Secured)")
    print(f" File Size    : {size} bytes")
    print(f" Last Modified: {mod_time}")
    print("-" * 40)
    print(" Active Threat Indicators:")
    
    if os.path.exists(target_log):
        with open(target_log, "r") as f:
            for line in f:
                if "ALERT" in line:
                    print(f"   -> {line.strip()}")
    print("=" * 40)

if __name__ == "__main__":
    render_dashboard()
