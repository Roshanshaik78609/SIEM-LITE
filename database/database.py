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

conn.commit()
conn.close()

print("Database initialized successfully!")