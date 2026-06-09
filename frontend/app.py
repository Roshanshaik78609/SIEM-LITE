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

    conn.close()

    alerts = []

    for row in rows:

        alerts.append({
            "timestamp": row[0],
            "type": row[1],
            "user": row[2],
            "severity": row[3]
        })

    return render_template(
        "index.html",
        alerts=alerts,
        total=len(alerts)
    )


if __name__ == "__main__":
    app.run(debug=True)