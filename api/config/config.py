from fastapi import FastAPI, APIRouter, Request, File, UploadFile, status, HTTPException
# from imagekitio import ImageKit
import uuid
import os
# import multipart
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# import requests


class ReuseableLibrary:
    BaseModel = BaseModel
    FastAPI = FastAPI
    APIRouter = APIRouter
    Request = Request
    File = File
    UploadFile = UploadFile
    # ImageKit = ImageKit
    uuid = uuid
    status = status
    HTTPException = HTTPException
    os = os
    # requests = requests
    # multipart = multipart
    load_dotenv = load_dotenv
    CORSMiddleware = CORSMiddleware
    origins = [
        "http://localhost:8000",  # frontend URL (adjust as needed)
        "http://127.0.0.1:8000",
        # add other origins if needed
    ]
    PROJECT_ID = ""
    LANGUAGE_CODE = "en"
    BOT_URL = ""
    headers = {"accept": "application/json", "content-type": "application/json"}
    API_V1 = "/api/v1"


rl = ReuseableLibrary
