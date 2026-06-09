from collections import defaultdict
from datetime import datetime
from log_collector import collect_logs
from alert_manager import save_alert


def detect_file_access():

    logs = collect_logs()

    accesses = defaultdict(list)

    for log in logs:

        if log["event"] == "FILE_ACCESS":

            user = log["user"]

            timestamp = datetime.strptime(
                log["timestamp"],
                "%Y-%m-%d %H:%M:%S"
            )

            accesses[user].append(timestamp)

    print("\n=== File Access Detection ===\n")

    for user, timestamps in accesses.items():

        timestamps.sort()

        for i in range(len(timestamps) - 4):

            first = timestamps[i]
            fifth = timestamps[i + 4]

            if (fifth - first).total_seconds() <= 30:

                print(
                    f"ALERT: Suspicious File Access detected on '{user}'"
                )

                save_alert(
                    "SUSPICIOUS_FILE_ACCESS",
                    user,
                    "MEDIUM"
                )

                break


if __name__ == "__main__":
    detect_file_access()