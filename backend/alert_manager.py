import sqlite3
from datetime import datetime, timedelta


def save_alert(alert_type, user, severity):

    conn = sqlite3.connect("../database/alerts.db")
    cursor = conn.cursor()

    current_time = datetime.now()

    # Check if a recent alert already exists
    cursor.execute(
        """
        SELECT last_alert_time
        FROM recent_alerts
        WHERE user = ? AND type = ?
        """,
        (user, alert_type)
    )

    result = cursor.fetchone()

    if result:

        last_alert_time = datetime.strptime(
            result[0],
            "%Y-%m-%d %H:%M:%S"
        )

        if current_time - last_alert_time < timedelta(minutes=5):

            print(
                f"Duplicate alert skipped for user: {user}"
            )

            conn.close()
            return

        cursor.execute(
            """
            UPDATE recent_alerts
            SET last_alert_time = ?
            WHERE user = ? AND type = ?
            """,
            (
                current_time.strftime("%Y-%m-%d %H:%M:%S"),
                user,
                alert_type
            )
        )

    else:

        cursor.execute(
            """
            INSERT INTO recent_alerts
            (user, type, last_alert_time)
            VALUES (?, ?, ?)
            """,
            (
                user,
                alert_type,
                current_time.strftime("%Y-%m-%d %H:%M:%S")
            )
        )

    cursor.execute(
        """
        INSERT INTO alerts
        (timestamp, type, user, severity)
        VALUES (?, ?, ?, ?)
        """,
        (
            current_time.strftime("%Y-%m-%d %H:%M:%S"),
            alert_type,
            user,
            severity
        )
    )

    conn.commit()
    conn.close()

    print(f"Alert saved for user: {user}")