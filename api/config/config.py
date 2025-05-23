from fastapi import FastAPI, status, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import uuid
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Any, Dict

load_dotenv()

origins = [
    "https://operachatbot.netlify.app",  # frontend URL (adjust as needed),
    "http://localhost:5173",
    # add other origins if needed
]

API_V1 = "api/v1"

# Chatbot Details
PROJECT_ID = os.getenv("PROJECT_ID")
LANGUAGE_CODE = "en-US"
PRIVATE_KEY_ID = os.getenv("PRIVATE_KEY_ID")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
CLIENT_EMAIL = os.getenv("CLIENT_EMAIL")
CLIENT_ID = os.getenv("CLIENT_ID")
AUTH_URL = os.getenv("AUTH_URL")
TOKEN_URL = os.getenv("TOKEN_URL")
AUTH_PROVIDER_X509_CERT_URL = os.getenv("AUTH_PROVIDER_X509_CERT_URL")
CLIENT_X509_CER_URL = os.getenv("CLIENT_X509_CER_URL")
UNIVERSE_DOMAIN = os.getenv("UNIVERSE_DOMAIN")