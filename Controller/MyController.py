from Request.RequestTemplate import User
from dotenv import load_dotenv
from jose import jwt, JWTError
from datetime import datetime, timedelta
import os

load_dotenv(verbose=True)


class MyController:
    @staticmethod
    async def test_path(value: int):
        return value

    @staticmethod
    async def test_param(*args):
        return sum(args)

    @staticmethod
    async def test_body(user: User):
        expire = datetime.utcnow() + timedelta(minutes=30)
        payload = {"sub": "dummy_user", "exp": expire}
        token = jwt.encode(payload, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
        return {"access_token": token, "token_type": "bearer"}
