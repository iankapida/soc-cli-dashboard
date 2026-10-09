import hashlib
import os

# Define a critical file we want to monitor for integrity
TARGET_FILE = "critical_config.json"

def create_dummy_config():
    """Create a baseline config file if it doesn't exist."""
    if not os.path.exists(TARGET_FILE):
        with open(TARGET_FILE, "w") as f:
                    f.write('{"admin_access": "enabled", "firewall_mode": "strict"}')

def calculate_file_hash(filepath):
    """Calculate the SHA-256 cryptographic hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def run_fim():
    print("[*] Initializing File Integrity Monitor (FIM)...")
    create_dummy_config()
    
    # Establish baseline hash
    baseline_hash = calculate_file_hash(TARGET_FILE)
    print(f"  [+] Baseline Established for {TARGET_FILE}")
    print(f"      SHA-256: {baseline_hash[:16]}...")
    
    # Simulate an attacker modifying the critical file
    print("\n[*] Simulating unauthorized file modification by an attacker...")
    with open(TARGET_FILE, "a") as f:
        f.write('\n# UNAUTHORIZED BACKDOOR ADDED')
        
    # Check integrity after modification
    current_hash = calculate_file_hash(TARGET_FILE)
    print(f"  [!] Current Hash : {current_hash[:16]}...")
    
    if baseline_hash != current_hash:
        print("  [!] INTEGRITY ALERT: Critical file tampering detected!")
        print("      File modification hash mismatch! Immediate forensic review required.\n")
    else:
        print("  [-] File integrity verified. No changes detected.\n")

if __name__ == "__main__":
    run_fim()
