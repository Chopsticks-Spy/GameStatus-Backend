from pydantic import BaseModel

class PlayerProfile(BaseModel):
    username: str
    password: str

class UpdateMMR(BaseModel):
    username: str
    score: int