
import time
from datetime import datetime

users = [
    "admin",
    "user1",
    "user2",
    "guest",
    "roshan"
]


def write_log(event, user):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} | {event} | user={user}"

    print(log_entry)

    with open("logs.txt", "a") as file:
        file.write(log_entry + "\n")


while True:

    # -----------------------------
    # Normal Activity
    # -----------------------------
    write_log("LOGIN_SUCCESS", "roshan")
    time.sleep(2)

    write_log("LOGIN_SUCCESS", "user1")
    time.sleep(2)

    write_log("FILE_ACCESS", "guest")
    time.sleep(2)

    write_log("LOGIN_SUCCESS", "admin")
    time.sleep(2)

    # -----------------------------
    # Brute Force Attack
    # -----------------------------
    for i in range(5):
        write_log("LOGIN_FAILED", "admin")
        time.sleep(1)

    time.sleep(5)

    # -----------------------------
    # Normal Activity
    # -----------------------------
    write_log("LOGIN_SUCCESS", "user2")
    time.sleep(2)

    write_log("FILE_ACCESS", "guest")
    time.sleep(2)

    # -----------------------------
    # Password Spray Attack
    # -----------------------------
    spray_users = ["admin", "user1", "user2", "guest", "roshan"]

    for user in spray_users:
        write_log("LOGIN_FAILED", user)
        time.sleep(1)

    time.sleep(5)

    # -----------------------------
    # Suspicious File Access
    # -----------------------------
    for i in range(5):
        write_log("FILE_ACCESS", "guest")
        time.sleep(1)

    time.sleep(5)

    # -----------------------------
    # Unauthorized Access Flood
    # -----------------------------
    for i in range(5):
        write_log("UNAUTHORIZED_ACCESS", "user1")
        time.sleep(1)

    time.sleep(5)

    # -----------------------------
    # Privilege Escalation
    # -----------------------------
    for i in range(3):
        write_log("PRIVILEGE_ESCALATION", "admin")
        time.sleep(1)

    time.sleep(10)

