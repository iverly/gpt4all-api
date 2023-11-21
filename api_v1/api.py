from api_v1.routes import completions, health
from fastapi import APIRouter

router = APIRouter()

router.include_router(completions.router)
router.include_router(health.router)
