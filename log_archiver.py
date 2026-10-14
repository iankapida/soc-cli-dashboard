# log_archiver.py
import os
import shutil
from datetime import datetime

def archive_logs(target_log="suspect_traffic.log", archive_dir="archives"):
    print(f"[*] Checking log status for: {target_log}")
    
    if not os.path.exists(target_log):
        print(f"    [!] Error: Log file {target_log} does not exist.")
        return
        
    # Create archive directory if it doesn't exist
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
        print(f"    [+] Created archive storage directory: {archive_dir}/")
        
    # Generate timestamped archive filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    archive_name = os.path.join(archive_dir, f"suspect_traffic_{timestamp}.bak")
    
    # Copy current log to archive and reset live log
    shutil.copy2(target_log, archive_name)
    print(f"    [+] Successfully archived log to: {archive_name}")
    
    # Clear the live log file for fresh telemetry collection
    with open(target_log, "w") as f:
        f.write(f"# Log reset and rotated by SOC Automation on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
    print(f"    [+] Live log {target_log} cleared and ready for new ingestion.")

if __name__ == "__main__":
    archive_logs()
