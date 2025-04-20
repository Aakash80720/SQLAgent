from fastapi import FastAPI, APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from app.core.session import get_db
from app.models import User
from app.schemas import UserCreate, UserRead, UserUpdate, UserDelete
from services.user_service import UserCreateService, UserReadService, UserUpdateService
from utils.repository import Repository

app = APIRouter()

@app.get("/", response_model=list[UserRead])
async def list_users(db: Session = Depends(get_db)):
    return await UserReadService(db).list_users()
    pass

@app.get("/{user_id}", response_model=UserRead)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user = await UserReadService(db).read(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return user

@app.post("/", response_model=UserRead)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        user = await UserCreateService(db).create(user)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    return user

@app.put("/{user_id}", response_model=UserRead)
async def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    try:
        user = await UserUpdateService(db).update(user_id, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return user

