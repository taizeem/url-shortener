from pydantic import BaseModel, HttpUrl
from datetime import datetime

class URLCreate(BaseModel):
    original_url: HttpUrl

class URLStatsResponse(BaseModel):
    short_code : str
    original_url: str
    clicks: int

class URLResponse(BaseModel):
    id : int
    original_url: str
    short_code: str