import re

def check_password_strength(password):
    print(f"[*] Analyzing password policy compliance...")
    
    if len(password) < 8:
        return "[!] Weak: Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return "[!] Weak: Must contain at least one uppercase letter."
    if not re.search(r"[0-9]", password):
        return "[!] Weak: Must contain at least one number."
    if not re.search(r"[!@#$%^&*]", password):
        return "[!] Weak: Must contain at least one special character."
        
    return "[+] Strong: Password meets all security requirements."

# Test a sample password
test_pass = "CyberSecure#2026"
print(check_password_strength(test_pass))
