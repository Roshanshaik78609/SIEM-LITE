import sqlite3

conn = sqlite3.connect("alerts.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    type TEXT,
    user TEXT,
    severity TEXT

)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS recent_alerts (

    user TEXT,
    type TEXT,
    last_alert_time TEXT

)
""")

conn.commit()
conn.close()

print("Database initialized successfully!")