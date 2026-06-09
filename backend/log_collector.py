from pathlib import Path


def collect_logs():

    log_file = Path("../agents/logs.txt")
    state_file = Path("log_state.txt")

    # Read last processed line
    with open(state_file, "r") as f:
        last_line = int(f.read().strip())

    # Read all log lines
    with open(log_file, "r") as f:
        lines = f.readlines()

    # Read only new lines
    new_lines = lines[last_line:]

    # Update state
    with open(state_file, "w") as f:
        f.write(str(len(lines)))

    logs = []

    for line in new_lines:

        parts = line.strip().split(" | ")

        if len(parts) == 3:

            logs.append({
                "timestamp": parts[0],
                "event": parts[1],
                "user": parts[2].replace("user=", "")
            })

    return logs


if __name__ == "__main__":
    collected_logs = collect_logs()

    for log in collected_logs:
        print(log)