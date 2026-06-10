from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():

    conn = sqlite3.connect("../database/alerts.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT timestamp, type, user, severity
        FROM alerts
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    alerts = []

    high = 0
    medium = 0
    low = 0

    # Alert Type Statistics
    type_stats = {
        "BRUTE_FORCE": 0,
        "PASSWORD_SPRAY": 0,
        "SUSPICIOUS_FILE_ACCESS": 0,
        "UNAUTHORIZED_ACCESS_FLOOD": 0,
        "PRIVILEGE_ESCALATION": 0
    }

    for row in rows:

        alert = {
            "timestamp": row[0],
            "type": row[1],
            "user": row[2],
            "severity": row[3]
        }

        alerts.append(alert)

        # Count severity
        if row[3].upper() == "HIGH":
            high += 1

        elif row[3].upper() == "MEDIUM":
            medium += 1

        elif row[3].upper() == "LOW":
            low += 1

        # Count alert types
        if row[1] in type_stats:
            type_stats[row[1]] += 1

    conn.close()

    return render_template(
    "index.html",
    alerts=alerts,
    total=len(alerts),
    high=high,
    medium=medium,
    low=low,
    type_stats=type_stats,
    engine_status="🟢 Running",
    refresh_time="Every 5 Seconds",

    brute_force=type_stats["BRUTE_FORCE"],
    password_spray=type_stats["PASSWORD_SPRAY"],
    file_access=type_stats["SUSPICIOUS_FILE_ACCESS"],
    unauthorized=type_stats["UNAUTHORIZED_ACCESS_FLOOD"],
    privilege=type_stats["PRIVILEGE_ESCALATION"]
)


if __name__ == "__main__":
    app.run(debug=True)