import sqlite3

DB_FILE = "soc_incidents.db"

def fetch_incidents():
    print(f"[*] Connecting to database: {DB_FILE}...\n")
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Query all stored incidents
    cursor.execute("SELECT id, source_ip, failure_count, severity, timestamp FROM incidents")
    records = cursor.fetchall()
    
    print(f"{'ID':<4} | {'Source IP':<15} | {'Failures':<8} | {'Severity':<8} | {'Timestamp'}")
    print("-" * 65)
    
    for row in records:
        inc_id, ip, count, severity, timestamp = row
        print(f"{inc_id:<4} | {ip:<15} | {count:<8} | {severity:<8} | {timestamp}")
        
    conn.close()

if __name__ == "__main__":
    fetch_incidents()
