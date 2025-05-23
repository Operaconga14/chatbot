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

# from imagekitio import ImageKit
import uuid
import os
import json
import base64

# import multipart
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


class ReuseableLibrary:
    BaseModel = BaseModel
    FastAPI = FastAPI
    APIRouter = APIRouter
    Request = Request
    Response = Response
    JSONResponse = JSONResponse
    Dict = Dict
    Any = Any
    File = File
    UploadFile = UploadFile
    GoogleRequest = GoogleRequest
    dialogflow = dialogflow
    GoogleAPICallError = GoogleAPICallError
    # ImageKit = ImageKit
    uuid = uuid
    status = status
    HTTPException = HTTPException
    os = os
    json = json
    base64 = base64
    requests = requests
    service_account = service_account
    # multipart = multipart
    load_dotenv = load_dotenv
    CORSMiddleware = CORSMiddleware
    origins = [
        f"{os.getenv('FRONTEND_URL')}",  # frontend URL (adjust as needed)
        "http://127.0.0.1:8000",
        "http://localhost:5173"
        # add other origins if needed
    ]
    headers = {"accept": "application/json", "content-type": "application/json"}
    API_V1 = "/api/v1"
    # Dialogflow
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


rl = ReuseableLibrary
