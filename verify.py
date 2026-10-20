import subprocess

def run_test():
    print("[*] Running automated validation for SOC CLI Dashboard...")
    try:
        result = subprocess.run(
            ["python3", "parser.py", "auth_sample.log"],
            capture_output=True,
            text=True,
            check=True
        )
        print("[+] Test Output:")
        print(result.stdout)
        print("[✓] Verification Passed: Script executed successfully.")
    except Exception as e:
        print(f"[X] Verification Failed: {e}")

if __name__ == "__main__":
    run_test()
