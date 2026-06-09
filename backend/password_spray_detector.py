from collections import defaultdict
from datetime import datetime
from log_collector import collect_logs
from alert_manager import save_alert


def detect_password_spray():

    logs = collect_logs()

    failed_users = defaultdict(set)

    for log in logs:

        if log["event"] == "LOGIN_FAILED":

            timestamp = datetime.strptime(
                log["timestamp"],
                "%Y-%m-%d %H:%M:%S"
            )

            minute = timestamp.strftime("%Y-%m-%d %H:%M")

            failed_users[minute].add(log["user"])

    print("\n=== Password Spray Detection ===\n")

    for minute, users in failed_users.items():

        if len(users) >= 5:

            print(
                f"ALERT: Password Spray detected ({len(users)} users)"
            )

            save_alert(
                "PASSWORD_SPRAY",
                "MULTIPLE_USERS",
                "HIGH"
            )


if __name__ == "__main__":
    detect_password_spray()