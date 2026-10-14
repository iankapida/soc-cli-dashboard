import hashlib

# Sample text or file data to check
data = "Confidential System Configuration v1.0"

# Generate a SHA-256 hash (digital fingerprint)
sha256_hash = hashlib.sha256(data.encode()).hexdigest()

print("[*] Computing cryptographic hash...")
print(f"[*] Data Content: {data}")
print(f"[+] SHA-256 Fingerprint: {sha256_hash}")
