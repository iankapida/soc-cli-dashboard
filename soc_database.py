import sqlite3

DB_NAME = "soc_incidents.db"

def init_db():
    """Initializes the SQLite database and creates the incidents table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            ip TEXT,
            action TEXT,
            abuse_score INTEGER,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_incident(timestamp, ip, action, abuse_score, status):
    """Inserts a security incident record into the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO incidents (timestamp, ip, action, abuse_score, status)
        VALUES (?, ?, ?, ?, ?)
    """, (timestamp, ip, action, abuse_score, status))
    conn.commit()
    conn.close()

def fetch_recent_incidents(limit=10):
    """Fetches recent incidents from the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT timestamp, ip, action, abuse_score, status 
        FROM incidents ORDER BY id DESC LIMIT ?
    """, (limit,))
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")
