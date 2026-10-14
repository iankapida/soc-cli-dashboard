# fim.py
import hashlib
import os

def calculate_file_hash(filepath):
    sha256_hash = hashlib.sha256()
    if not os.path.exists(filepath):
        return None
    
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
            
    return sha256_hash.hexdigest()

def verify_integrity(filepath, baseline_hash):
    print(f"[*] Monitoring file integrity for: {filepath}")
    current_hash = calculate_file_hash(filepath)
    
    print(f"    Baseline Hash : {baseline_hash}")
    print(f"    Current Hash  : {current_hash}")
    
    if current_hash == baseline_hash:
        print("    [+] Status: INTEGRITY VERIFIED (No unauthorized changes)")
    else:
        print("    [!] ALERT: FILE TAMPERING DETECTED!")

if __name__ == "__main__":
    target_file = "suspect_traffic.log"
    
    # Establish baseline hash of our log file
    baseline = calculate_file_hash(target_file)
    if baseline:
        verify_integrity(target_file, baseline)
    else:
        print(f"[!] Target file {target_file} not found.")
