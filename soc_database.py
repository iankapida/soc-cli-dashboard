import sqlite3
import datetime

# Step 1: Initialize local SQLite database for persistent SOC event storage
db_name = "soc_incidents.db"
print(f"[*] Connecting to local relational database: {db_name}")

conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Step 2: Create a structured security incidents schema
cursor.execute('''
    CREATE TABLE IF NOT EXISTS incidents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        source_ip TEXT,
        threat_score INTEGER,
        ttp TEXT,
        status TEXT
    )
''')
conn.commit()

# Step 3: Insert normalized security telemetry into the database vault
sample_incidents = [
    (datetime.datetime.now().isoformat(), "192.168.100.45", 88, "T1110 - Brute Force", "Isolated"),
    (datetime.datetime.now().isoformat(), "203.0.113.50", 45, "T1078 - Valid Accounts", "Monitoring"),
    (datetime.datetime.now().isoformat(), "198.51.100.22", 92, "T1210 - Exploitation", "Contained")
]

print("[*] Committing parsed incident payloads to database vault...")
cursor.executemany('''
    INSERT INTO incidents (timestamp, source_ip, threat_score, ttp, status)
    VALUES (?, ?, ?, ?, ?)
''', sample_incidents)
conn.commit()

# Step 4: Perform a simulated Threat Hunting SQL Query
print("\n[*] Executing Threat Hunt Query: Selecting high-severity incidents (Score >= 80)...")
cursor.execute("SELECT source_ip, threat_score, ttp, status FROM incidents WHERE threat_score >= 80")
high_severity_records = cursor.fetchall()

for row in high_severity_records:
    print(f"    [!] Target IP: {row[0]} | Score: {row[1]}/100 | TTP: {row[2]} | Status: {row[3]}")

# Close database connection cleanly
conn.close()
print(f"\n[+] Database transaction complete. {len(sample_incidents)} records secured in local vault.")
