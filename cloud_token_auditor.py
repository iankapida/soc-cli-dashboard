import base64
import json

# Simulated Cloud API JWT tokens
SAMPLE_TOKENS = [
    # Normal user token
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWxpY2UiLCJyb2xlIjoidXNlciIsImV4cCI6MTgwMDAwMDAwMH0.signature1",
    # Malformed / Suspicious token payload string
    "malformed_token_string_example"
]

def decode_jwt_payload(token_str):
    """Safely decode token payload with error handling."""
    try:
        parts = token_str.split(".")
        if len(parts) != 3:
            return None, "Malformed Token Structure (Not a valid 3-part JWT)"
        
        payload_part = parts[1]
        payload_part += '=' * (-len(payload_part) % 4)
        decoded_bytes = base64.b64decode(payload_part)
        payload_data = json.loads(decoded_bytes.decode('utf-8'))
        return payload_data, "SUCCESS"
    except Exception as e:
        return None, f"Decoding/Parsing Error: {str(e)}"

def audit_token(token_str):
    """Audit token claims or flag structural tampering."""
    print(f"[*] Inspecting Token: {token_str[:30]}...")
    claims, status = decode_jwt_payload(token_str)
    
    if status != "SUCCESS":
        print(f"  [!] CLOUD SECURITY ALERT: Invalid or tampered token detected!")
        print(f"      Reason: {status}\n")
        return

    user = claims.get("user", "unknown")
    role = claims.get("role", "standard")
    print(f"    User: {user} | Role: {role}")
    print(f"  [-] Token claims verified successfully.\n")

def run_token_auditor():
    print("[*] Initializing Cloud API & JWT Security Auditor...\n")
    for token in SAMPLE_TOKENS:
        audit_token(token)

if __name__ == "__main__":
    run_token_auditor()
