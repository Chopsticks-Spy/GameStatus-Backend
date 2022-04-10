from pydantic import BaseModel

class PlayerProfile(BaseModel):
    username: str
    password: str

class UpdateMMR(BaseModel):
    username: str
    score: int

class GameStatus(BaseModel):
    isActive: bool
    isWin: int
    activeLaser: list

class ScoreboardInstance(BaseModel):
    name: str
    laser: list
    hp: int
    time: float