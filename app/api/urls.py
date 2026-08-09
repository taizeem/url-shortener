from fastapi import APIRouter
from app.schemas.url import URLCreate


router = APIRouter(
    prefix="/urls",
    tags=["URLS"],
)

@router.post("/")

def create_short_url(data: URLCreate):
    return {
        "orignial_url": str(data.original_url)
    }