import sqlite3
from datetime import datetime


def save_alert(alert_type, user, severity):

    conn = sqlite3.connect("../database/alerts.db")
    cursor = conn.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        """
        INSERT INTO alerts
        (timestamp, type, user, severity)
        VALUES (?, ?, ?, ?)
        """,
        (
            timestamp,
            alert_type,
            user,
            severity
        )
    )

    conn.commit()
    conn.close()

    print(f"Alert saved for user: {user}")