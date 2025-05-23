from fastapi import FastAPI, status, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import uuid
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Any, Dict

origins = [
    "https://operachatbot.netlify.app",  # frontend URL (adjust as needed),
    "http://localhost:5173",
    # add other origins if needed
]

API_V1 = "api/v1"
