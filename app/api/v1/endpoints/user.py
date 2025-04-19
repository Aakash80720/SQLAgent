from fastapi import FastAPI, APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from app.core.session import get_db
from app.models import User
from app.schemas import UserCreate, UserRead
from services.user_service import UserCreateService
from utils.repository import Repository

app = APIRouter()

@app.get("/{user_id}", response_model=UserRead)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalars().first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/", response_model=UserRead)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        user = await UserCreateService(db).create(user)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    return user