from collections import defaultdict
from datetime import datetime
from log_collector import collect_logs
from alert_manager import save_alert


def detect_privilege_escalation():

    logs = collect_logs()

    escalations = defaultdict(list)

    for log in logs:

        if log["event"] == "PRIVILEGE_ESCALATION":

            user = log["user"]

            timestamp = datetime.strptime(
                log["timestamp"],
                "%Y-%m-%d %H:%M:%S"
            )

            escalations[user].append(timestamp)

    print("\n=== Privilege Escalation Detection ===\n")

    for user, timestamps in escalations.items():

        timestamps.sort()

        for i in range(len(timestamps) - 2):

            first = timestamps[i]
            third = timestamps[i + 2]

            if (third - first).total_seconds() <= 30:

                print(
                    f"ALERT: Privilege Escalation detected on '{user}'"
                )

                save_alert(
                    "PRIVILEGE_ESCALATION",
                    user,
                    "HIGH"
                )

                break


if __name__ == "__main__":
    detect_privilege_escalation()