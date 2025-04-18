# Initialize the endpoints package
from fastapi import APIRouter
from . import user

router = APIRouter()

router.include_router(user.app, prefix="/users", tags=["users"])