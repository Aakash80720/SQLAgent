from fastapi import FastAPI, APIRouter

app = APIRouter()

@app.get("/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id, "username": "johndoe"}

@app.post("/")
async def create_user(user: dict):
    return {"user_id": 1, "username": user["username"]}