# Initialize the v1 API package
from fastapi import APIRouter
from .endpoints import router as endpoints_router

router = APIRouter()
router.include_router(endpoints_router, prefix="/v1", tags=["v1"])