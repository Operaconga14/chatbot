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


API_V1 = "/api/v1"