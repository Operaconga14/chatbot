from fastapi import FastAPI, APIRouter, Request, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from google.cloud import dialogflow_v2 as dialogflow
from imagekitio import ImageKit
import uuid
import os
import multipart
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests


class ReuseableLibrary:
    BaseModel = BaseModel
    FastAPI = FastAPI
    APIRouter = APIRouter
    Request = Request
    File = File
    UploadFile = UploadFile
    StaticFiles = StaticFiles
    Jinja2Templates = Jinja2Templates
    HTMLResponse = HTMLResponse
    dialogflow = dialogflow
    ImageKit = ImageKit
    uuid = uuid
    os = os
    requests = requests
    multipart = multipart
    load_dotenv = load_dotenv
    CORSMiddleware = CORSMiddleware
    origins = [
        "http://localhost:8000",  # frontend URL (adjust as needed)
        "http://127.0.0.1:8000",
        # add other origins if needed
    ]
    PROJECT_ID = "your-dialogflow-project-id"
    LANGUAGE_CODE = "en"
    BOT_URL = "https://webhook.botpress.cloud/d969a90b-92ae-4e87-b7ac-d21fbda2fc95"
    headers = {"accept": "application/json", "content-type": "application/json"}
    API_V1="/api/v1"


rl = ReuseableLibrary


def get_context(request):
    return {"request": request}
