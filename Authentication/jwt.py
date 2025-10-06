from jose import jwt, JWTError
from datetime import datetime, timedelta
import os

async def create_token(name):
    expire = datetime.utcnow() + timedelta(minutes=30)
    payload = {"sub": name, "exp": expire}
    token = jwt.encode(payload, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return {"access_token": token, "token_type": "bearer"}

async def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
        return payload
    except JWTError as e:
        raise ValueError("Invalid or expired token") from e