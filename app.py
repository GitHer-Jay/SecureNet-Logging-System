from fastapi import FastAPI
import threading

from core.database import create_table
from core.log_manager import add_log
from core.verifier import verify_logs
from agent.host_agent import start_agent

app = FastAPI()

# Create DB table on startup
create_table()


@app.get("/")
def home():
    return {"message": "SecureNet Logging System Running"}


@app.post("/log")
def log(event: str, description: str, user: str, ip: str):
    root = add_log(event, description, user, ip)
    return {"status": "added", "merkle_root": root}


@app.get("/verify")
def verify():
    result = verify_logs()
    return {"result": result}


# 🔥 START AGENT AUTOMATICALLY
@app.on_event("startup")
def start_background_agent():
    thread = threading.Thread(target=start_agent, daemon=True)
    thread.start()