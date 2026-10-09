import json

# Simulated enterprise user directory / IAM database
USER_DIRECTORY = [
    {"username": "alice", "role": "standard_user", "mfa_enabled": True, "last_login": "2026-09-18"},
    {"username": "bob", "role": "standard_user", "mfa_enabled": True, "last_login": "2026-09-10"},
    # An anomalous or high-risk account with missing MFA and elevated privileges
    {"username": "svc_backup", "role": "domain_admin", "mfa_enabled": False, "last_login": "2026-09-18"},
    {"username": "charlie", "role": "guest", "mfa_enabled": False, "last_login": "2026-08-01"}
]

def audit_iam_accounts():
    print("[*] Initializing IAM Privilege & Access Control Auditor...\n")
    
    anomalies_found = 0
    
    for user in USER_DIRECTORY:
        uname = user["username"]
        role = user["role"]
        mfa = user["mfa_enabled"]
        
        print(f"[*] Inspecting User: '{uname}' | Role: {role} | MFA: {mfa}")
        
        # Rule 1: High privilege accounts must have MFA enabled
        if role in ["domain_admin", "administrator"] and not mfa:
            anomalies_found += 1
            print(f"  [!] IAM SECURITY ALERT: High-privilege account '{uname}' lacks Multi-Factor Authentication (MFA)!")
            print(f"      Risk: High vulnerability to credential compromise.\n")
            
        # Rule 2: Inactive or guest accounts with suspicious attributes
        elif role == "guest" and not mfa:
            print(f"  [-] Note: Guest account '{uname}' has standard guest restrictions.")
            print(f"      Status: Low risk.\n")
        else:
            print(f"  [-] Access controls verified. Account parameters compliant.\n")
            
    print("=" * 50)
    print(f"[*] IAM Audit Completed. Total high-risk anomalies flagged: {anomalies_found}")
    print("=" * 50)

if __name__ == "__main__":
    audit_iam_accounts()
