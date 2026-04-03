import time
from core.log_manager import add_log

def start_agent():
    while True:
        add_log(
            event="AUTO_EVENT",
            description="System generated log",
            user="system",
            ip="127.0.0.1"
        )
        time.sleep(15)