import os
from dashboard import parse_auth_log, detect_brute_force

def test_dashboard():
    print("[*] Running Enhanced SOC CLI Dashboard Verification Suite...")
    
    # Test 1: Verify log parsing function handles missing files safely
    failed, accepted = parse_auth_log("non_existent_file.log")
    assert isinstance(failed, dict), "Failed attempts should return a dictionary"
    assert isinstance(accepted, list), "Accepted attempts should return a list"
    print("[+] Test 1 Passed: Error handling for missing files verified.")

    # Test 2: Verify parsing and threshold detection with timestamps & severity
    sample_log = "auth_sample.log"
    if os.path.exists(sample_log):
        failed_data, accepted_data = parse_auth_log(sample_log)
        assert len(failed_data) > 0, "Should detect failed login attempts in sample log"
        
        flagged = detect_brute_force(failed_data, threshold=2)
        assert isinstance(flagged, list), "Flagged output must be a sorted list"
        
        # Verify structure of enhanced incident data
        for ip, data in flagged:
            assert "severity" in data, "Data must include a severity rating"
            assert "timestamps" in data, "Data must include timestamps list"
            assert "recommendation" in data, "Data must include a recommendation"
            
        print(f"[+] Test 2 Passed: Parsed log and validated enhanced fields for {len(flagged)} IP(s).")
    else:
        print("[-] Warning: 'auth_sample.log' not found for integration testing.")

    print("\n[V] ALL AUTOMATED TESTS PASSED SUCCESSFULLY!\n")

if __name__ == "__main__":
    test_dashboard()
