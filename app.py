from fastapi import FastAPI
from core.database import create_table
from core.log_manager import add_log
from core.verifier import verify_logs

app = FastAPI()

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