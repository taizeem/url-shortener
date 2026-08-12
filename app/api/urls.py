from fastapi import APIRouter, Depends, HTTPException
from app.schemas.url import URLCreate
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse

from app.core.database import get_db
from app.models.urls import URL
from app.schemas.url import URLCreate, URLStatsResponse, URLResponse
from app.utils.short_code import generate_short_code


router = APIRouter(
    prefix="/urls",
    tags=["URLS"],
)

@router.post("/",status_code=201,response_model=URLResponse)

def create_short_url(data: URLCreate, db:Session = Depends(get_db)):
    
    existing_url = db.query(URL).filter(
        URL.original_url == str(data.original_url)
    ).first()

    if existing_url:
        return{
            "id": existing_url.id,
            "original_url": existing_url.original_url,
            "short_code": existing_url.short_code
        }

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

@router.get("/{short_code}/stats", response_model=URLStatsResponse)
def get_url_stats(
    short_code: str,
    db: Session = Depends(get_db),
):
    url = db.query(URL).filter(URL.short_code == short_code).first()

    if not url:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found",
        )

    return url

@router.get("/{short_code}")
def redirect_to_url(
    short_code: str,
    db: Session = Depends(get_db)
):
    url = db.query(URL).filter(URL.short_code == short_code).first()

    if not url:
        raise HTTPException(
            status_code= 404,
            detail= "Short URL not found"
        )
    url.clicks += 1
    db.commit()
    return RedirectResponse(url.original_url)