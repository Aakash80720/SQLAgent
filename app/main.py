from fastapi import FastAPI
from fastapi import APIRouter, Depends, HTTPException
from app.api.v1 import router as api_router
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI CRUD application!"}

app.include_router(api_router, prefix="/api", tags=["api"])