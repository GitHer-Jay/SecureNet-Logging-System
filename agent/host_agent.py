import time
import random
from core.log_manager import add_log

events = ["LOGIN", "FILE_ACCESS", "LOGOUT", "ERROR", "NETWORK"]

users = ["admin", "user1", "guest"]

ips = ["192.168.1.1", "10.0.0.5", "172.16.0.2"]


def generate_log():
    event = random.choice(events)
    desc = f"{event} event detected"
    user = random.choice(users)
    ip = random.choice(ips)

    add_log(event, desc, user, ip)


def start_agent():
    print("🚀 Agent started...")

    while True:
        generate_log()
        print("Log generated...")
        time.sleep(10)  # every 10 seconds