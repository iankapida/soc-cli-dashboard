import subprocess
import sys

def run_test():
    print("[*] Running automated validation suite for SOC CLI Dashboard...")
    try:
        result = subprocess.run(
            ["python3", "parser.py", "auth_sample.log"],
            capture_output=True,
            text=True,
            check=True
        )
        output = result.stdout
        print("[+] Test Execution Output:\n")
        print(output)

        # Assertions to verify correct parsing
        assert "Total Events Processed : 6" in output, "Assertion Failed: Event count mismatch"
        assert "Successful Logins     : 2" in output, "Assertion Failed: Successful login count mismatch"
        assert "Failed Login Attempts : 4" in output, "Assertion Failed: Failed login count mismatch"
        assert "IP: 185.220.101.5 | Failed Attempts: 3" in output, "Assertion Failed: Threat detection mismatch"

        print("[✓] ALL ASSERTIONS PASSED: Logic, counts, and threat detection verified.")

    except AssertionError as ae:
        print(f"[X] Validation Error: {ae}")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"[X] Execution Error: Script exited with code {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"[X] Verification Failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_test()
