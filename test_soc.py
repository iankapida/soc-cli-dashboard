import pytest
from threat_intel import check_ip_reputation

def test_clean_ip_reputation():
    result = check_ip_reputation("192.168.1.1")
    assert result["status"] == "CLEAN"
    assert result["abuse_score"] == 0

def test_suspicious_ip_reputation():
    result = check_ip_reputation("185.220.101.5")
    assert result["status"] == "SUSPICIOUS"
    assert result["abuse_score"] > 0

def test_response_keys():
    result = check_ip_reputation("10.0.0.1")
    assert "ip" in result
    assert "abuse_score" in result
    assert "status" in result
