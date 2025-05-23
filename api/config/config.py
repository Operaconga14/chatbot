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
        "https://operachatbot.netlify.app",  # frontend URL (adjust as needed)
        "http://127.0.0.1:8000",
        "http://localhost:5173"
        # add other origins if needed
    ]
    headers = {"accept": "application/json", "content-type": "application/json"}
    API_V1 = "/api/v1"
    # Dialogflow


rl = ReuseableLibrary
