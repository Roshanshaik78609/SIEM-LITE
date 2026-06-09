from collections import defaultdict
from datetime import datetime
from log_collector import collect_logs
from alert_manager import save_alert


def detect_brute_force():

    logs = collect_logs()

    failed_logins = defaultdict(list)

    for log in logs:

        if log["event"] == "LOGIN_FAILED":

            user = log["user"]

            timestamp = datetime.strptime(
                log["timestamp"],
                "%Y-%m-%d %H:%M:%S"
            )

            failed_logins[user].append(timestamp)

    print("\n=== Threat Detection Results ===\n")

    for user, timestamps in failed_logins.items():

        timestamps.sort()

        for i in range(len(timestamps) - 4):

            first = timestamps[i]
            fifth = timestamps[i + 4]

            difference = (fifth - first).total_seconds()

            if difference <= 30:

                print(
                    f"ALERT: Brute Force Attack detected on '{user}'"
                )

                save_alert(
                    "BRUTE_FORCE",
                    user,
                    "HIGH"
                )

                break


if __name__ == "__main__":
    detect_brute_force()