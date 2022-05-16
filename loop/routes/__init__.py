from fastapi import APIRouter, Depends

from .users import router as users_router

router = APIRouter()
router.include_router(users_router)
