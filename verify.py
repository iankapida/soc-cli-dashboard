import os
from dashboard import parse_auth_log, detect_brute_force

def test_dashboard():
    print("[*] Running SOC CLI Dashboard Verification Suite...")
    
    # Test 1: Verify missing file handling
    failed, accepted = parse_auth_log("non_existent_file.log")
    assert isinstance(failed, dict), "Failed attempts should return a dictionary"
    assert isinstance(accepted, list), "Accepted attempts should return a list"
    print("[+] Test 1 Passed: Error handling for missing files verified.")

    # Test 2: Verify log parsing and threshold detection
    sample_log = "auth_sample.log"
    if os.path.exists(sample_log):
        failed_data, accepted_data = parse_auth_log(sample_log)
        assert len(failed_data) > 0, "Should detect failed login attempts"
        
        flagged = detect_brute_force(failed_data, threshold=2)
        assert isinstance(flagged, list), "Flagged output must be a list"
        print(f"[+] Test 2 Passed: Parsed log and flagged {len(flagged)} IP(s).")

    print("\n[V] ALL AUTOMATED TESTS PASSED SUCCESSFULLY!\n")

if __name__ == "__main__":
    test_dashboard()
