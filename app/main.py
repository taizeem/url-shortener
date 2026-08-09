from fastapi import FastAPI
from app.core.config import settings
from app.api.urls import router as urls_router

app = FastAPI(
    title = settings.app_name,
    version = settings.app_version
)
app.include_router(urls_router)

    
