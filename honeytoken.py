# honeytoken.py
import os
from datetime import datetime

def deploy_and_monitor_honeytoken(token_file="aws_credentials_backup.json"):
    print(f"[*] Deploying and monitoring canary honeytoken: {token_file}")
    
    # Create the decoy file if it doesn't exist
    if not os.path.exists(token_file):
        decoy_data = {
            "aws_access_key_id": "AKIAIOSFODNN7EXAMPLE",
            "aws_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            "region": "us-east-1",
            "note": "CONFIDENTIAL - PRODUCTION BACKUP DO NOT ACCESS"
        }
        import json
        with open(token_file, "w") as f:
            json.dump(decoy_data, f, indent=4)
        print(f"    [+] Honeytoken deployed successfully.")
        
    # Simulate tripwire check (checking file access logs or modification times)
    file_stat = os.stat(token_file)
    access_time = datetime.fromtimestamp(file_stat.st_atime).strftime('%Y-%m-%d %H:%M:%S')
    
    print("-" * 50)
    print(" >>> TRIPWIRE MONITOR STATUS: ARMED <<<")
    print(f" Target File : {token_file}")
    print(f" Last Access : {access_time}")
    print(" Status      : INTACT (No unauthorized read attempts detected)")
    print("-" * 50)

if __name__ == "__main__":
    deploy_and_monitor_honeytoken()
