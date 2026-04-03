import threading
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from agent.host_agent import start_agent
from core.database import create_table
from core.log_manager import add_log
from core.verifier import verify_logs
from core.get_logs import get_logs

app = FastAPI()

# CORS (frontend fix)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    return {"result": verify_logs()}

@app.get("/logs")
def logs():
    return get_logs()

threading.Thread(target=start_agent, daemon=True).start()