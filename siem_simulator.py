import sqlite3

def detect_threshold_alerts(threshold=3):
    conn = sqlite3.connect('soc_incidents.db')
    cursor = conn.cursor()
    
    # SIEM Alert Rule: Detect IPs exceeding failure thresholds
    query = "SELECT source_ip, failure_count, severity, timestamp FROM incidents WHERE failure_count > ?"
    
    print(f"[*] Executing SIEM Alert Rule: Threshold > {threshold} failed attempts")
    cursor.execute(query, (threshold,))
    results = cursor.fetchall()
    
    print(f"[+] Alert Triggered! Found {len(results)} high-risk IPs exceeding threshold:")
    for row in results:
        print(f"   -> ALERT: IP {row[0]} | Failures: {row[1]} | Severity: {row[2]} | Time: {row[3]}")
        
    conn.close()

if __name__ == "__main__":
    detect_threshold_alerts(3)
