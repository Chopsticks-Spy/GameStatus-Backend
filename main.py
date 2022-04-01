from fastapi import FastAPI
from pydantic import BaseModel
from FileOp import getData,saveData

app = FastAPI()
Profile = getData('profile.json')

class PlayerProfile(BaseModel):
    username: str
    password: str

@app.get("/")
async def get_player_profile():
    Profile = getData('profile.json')
    return Profile

@app.post("/")
async def create_new_account(new_player:PlayerProfile):
    try:
        new_player = new_player.dict()

        new_id = str(Profile["latetest_id"])
        while len(new_id) < 4:
            new_id = '0' + new_id
        
        new_account = {
            "username": new_player["username"],
            "uid": new_id,
            "password": new_player["password"],
            "score": 0
        }
        Profile["data"][new_player["username"].lower()] = new_account
    except:
        return {"Error":"Try Again!"}
    else:
        Profile["latetest_id"] += 1
        saveData('profile.json',Profile)
        return new_account
