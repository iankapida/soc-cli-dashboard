import pytest
import os
from threat_intel import check_ip_reputation
from soc_database import init_db, log_incident, fetch_recent_incidents, DB_NAME

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

def test_database_logging():
    init_db()
    assert os.path.exists(DB_NAME)
    
    # Insert test record
    log_incident("12:00:00", "192.168.1.99", "TEST_ALERT", 50, "SUSPICIOUS")
    
    # Retrieve and verify
    records = fetch_recent_incidents(limit=1)
    assert len(records) > 0
    assert records[0][1] == "192.168.1.99"
    assert records[0][2] == "TEST_ALERT"
