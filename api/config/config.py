from fastapi import (
    FastAPI,
    status,
    HTTPException,
    APIRouter
)

origins = [
    "https://operachatbot.netlify.app",  # frontend URL (adjust as needed),
    "http://localhost:5173",
    # add other origins if needed
]

API_V1 = "api/v1"
