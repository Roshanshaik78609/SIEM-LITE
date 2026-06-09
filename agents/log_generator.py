import random
import time
from datetime import datetime

events = [
    "FILE_ACCESS",
    "FILE_ACCESS",
    "FILE_ACCESS",
    "FILE_ACCESS",
    "LOGIN_SUCCESS",
    "LOGIN_FAILED"
]

users = [
    "admin"
]

while True:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    event = random.choice(events)
    user = random.choice(users)

    log_entry = f"{timestamp} | {event} | user={user}"

    print(log_entry)

    with open("logs.txt", "a") as file:
        file.write(log_entry + "\n")

    time.sleep(2)