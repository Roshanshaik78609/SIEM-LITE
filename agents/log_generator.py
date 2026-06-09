import random
import time
from datetime import datetime

events = [
    "LOGIN_FAILED",
    "LOGIN_FAILED",
    "LOGIN_FAILED",
    "LOGIN_FAILED",
    "LOGIN_FAILED",
    "LOGIN_SUCCESS"
]

users = [
    "admin",
    "user1",
    "user2",
    "guest",
    "roshan"
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