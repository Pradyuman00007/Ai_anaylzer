from fastapi import Request, HTTPException, Depends
from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

limiter = Limiter(key_func=get_remote_address)
security = HTTPBasic()

# Hardcoded credentials for demo
USERNAME = "admin"
PASSWORD = "password123"

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, USERNAME)
    correct_password = secrets.compare_digest(credentials.password, PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
