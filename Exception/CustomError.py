from pydantic import BaseModel

class CustomError(BaseModel):
    error: str
    path: str
    type: str