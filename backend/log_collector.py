def collect_logs():
    logs = []

    with open("../agents/logs.txt", "r") as file:
        for line in file:
            parts = line.strip().split(" | ")

            if len(parts) == 3:
                timestamp = parts[0]
                event = parts[1]
                user = parts[2].replace("user=", "")

                logs.append({
                    "timestamp": timestamp,
                    "event": event,
                    "user": user
                })

    return logs


if __name__ == "__main__":
    collected_logs = collect_logs()

    for log in collected_logs:
        print(log)