from fastapi import (
    FastAPI,
    APIRouter,
    Request,
    Response,
    File,
    UploadFile,
    status,
    HTTPException,
)
from fastapi.responses import JSONResponse
import uuid
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request as GoogleRequest
from google.api_core.exceptions import GoogleAPICallError
from google.cloud import dialogflow_v2 as dialogflow

load_dotenv()

# origins = [
#     "https://operachatbot.netlify.app",  # frontend URL (adjust as needed)
#     "http://localhost:5173",
#     # add other origins if needed
# ]

# PROJECT_ID = os.getenv("PROJECT_ID")
# LANGUAGE_CODE = "en-US"
# PRIVATE_KEY_ID = os.getenv("PRIVATE_KEY_ID")
# PRIVATE_KEY = os.getenv("PRIVATE_KEY")
# CLIENT_EMAIL = os.getenv("CLIENT_EMAIL")
# CLIENT_ID = os.getenv("CLIENT_ID")
# AUTH_URL = os.getenv("AUTH_URL")
# TOKEN_URL = os.getenv("TOKEN_URL")
# AUTH_PROVIDER_X509_CERT_URL = os.getenv("AUTH_PROVIDER_X509_CERT_URL")
# CLIENT_X509_CER_URL = os.getenv("CLIENT_X509_CER_URL")
# UNIVERSE_DOMAIN = os.getenv("UNIVERSE_DOMAIN")
# headers = {"accept": "application/json", "content-type": "application/json"}
# API_V1 = "/api/v1"


# credentials = {
#     "type": "service_account",
#     "project_id": PROJECT_ID,
#     "private_key_id": PRIVATE_KEY_ID,
#     "private_key": PRIVATE_KEY,
#     "client_id": CLIENT_ID,
#     "client_email": CLIENT_EMAIL,
#     "auth_uri": AUTH_URL,
#     "token_uri": TOKEN_URL,
#     "auth_provider_x509_cert_url": AUTH_PROVIDER_X509_CERT_URL,
#     "client_x509_cert_url": CLIENT_X509_CER_URL,
#     "universe_domain": UNIVERSE_DOMAIN,
# }


# creds = service_account.Credentials.from_service_account_info(credentials)
# scoped_cred = creds.with_scopes(["https://www.googleapis.com/auth/dialogflow"])
# scoped_cred.refresh(GoogleRequest())

# session_client = dialogflow.SessionsClient(credentials=scoped_cred)
