from fastapi import APIRouter, Depends
from app.schemas.url import URLCreate
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.urls import URL
from app.schemas.url import URLCreate
from app.utils.short_code import generate_short_code


router = APIRouter(
    prefix="/urls",
    tags=["URLS"],
)

@router.post("/")

def create_short_url(data: URLCreate, db:Session = Depends(get_db)):
    short_code = generate_short_code()
    url = URL(
        original_url = str(data.original_url),
        short_code = short_code,
    )

    db.add(url)
    db.commit()
    db.refresh(url)

    return {
        "id": url.id,
        "original_url": url.original_url,
        "short_code": url.short_code
    }
    