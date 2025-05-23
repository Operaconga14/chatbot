from api.config.config import rl
from google.auth.transport.requests import Request
from api.controller.chat_controller import generate_session_id
import os


# Initailize fastapi
app = rl.FastAPI(
    title="Chatbot API",
    version="1.0.0",
    summary="Chat bot API Documentation and Testing",
)

# Initialize middlware
app.add_middleware(
    rl.CORSMiddleware,
    allow_origins=rl.origins,  # or ["*"] to allow all origins (not recommended for prod)
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # allowed HTTP methods
    allow_headers=["*"],  # allowed headers
)

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

private_key = PRIVATE_KEY.replace("\\n", "\n")

# Authenticate rl.DialogFlow
credentials = {
    "type": "service_account",
    "project_id": PROJECT_ID,
    "private_key_id": PRIVATE_KEY_ID,
    "private_key": private_key,
    "client_id": CLIENT_ID,
    "client_email": CLIENT_EMAIL,
    "auth_uri": AUTH_URL,
    "token_uri": TOKEN_URL,
    "auth_provider_x509_cert_url": AUTH_PROVIDER_X509_CERT_URL,
    "client_x509_cert_url": CLIENT_X509_CER_URL,
    "universe_domain": UNIVERSE_DOMAIN,
}

# Initialize Dialogflow client
creds = rl.service_account.Credentials.from_service_account_info(credentials)
scoped_cred = creds.with_scopes(["https://www.googleapis.com/auth/dialogflow"])
scoped_cred.refresh(rl.GoogleRequest())

session_client = rl.dialogflow.SessionsClient(credentials=scoped_cred)


# Chat request schema
class ChatRequest(rl.BaseModel):
    message: str


#  Testing API
@app.get(f"{rl.API_V1}", tags=["Test"], description="Route for testing API")
def read_root():
    return rl.HTTPException(
        status_code=rl.status.HTTP_200_OK, detail="Welcome to Chatbot"
    )


# Chat Id
@app.post(
    f"{rl.API_V1}/chat",
    tags=["Chatbot"],
    description="Conversation API first generating session id (chat_id)",
)
async def chat(response: rl.Response):
    # Generate SessionId
    session_id = generate_session_id()
    # print("Session Id :", session_id)

    # store the session id into cookies
    response.set_cookie("session_id", session_id)
    return session_id


@app.post(
    f"{rl.API_V1}/chat/conversation",
    tags=["Chatbot"],
    description="Conversational chat with chatobt",
)
async def conversational_chat(chat_request: ChatRequest, request: rl.Request):
    try:
        # Get user message from request
        data = await request.json()
        user_message = data.get("message")

        if not user_message:
            return rl.JSONResponse({"error": "No message provided"}, status_code=400)

        # Generate or get session ID
        session_id = request.cookies.get("session_id")
        if not session_id:
            session_id = str(uuid.uuid4())

        # Create session path
        session = session_client.session_path(PROJECT_ID, session_id)

        # Create text input
        text_input = rl.dialogflow.TextInput(
            text=user_message,
            language_code=LANGUAGE_CODE,
        )
        query_input = rl.dialogflow.QueryInput(text=text_input)

        # Send request to Dialogflow
        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

        # Extract response
        fulfillment_text = response.query_result.fulfillment_text
        detected_intent = response.query_result.intent.display_name

        # Create response
        response_data = {
            "session_id": session_id,
            "user_message": user_message,
            "bot_response": fulfillment_text,
            "detected_intent": detected_intent,
        }

        # Set session_id in cookies
        res = rl.JSONResponse(content=response_data, status_code=200)
        res.set_cookie(key="session_id", value=session_id)

        return res

    except rl.GoogleAPICallError as e:
        return rl.JSONResponse(
            {"error": f"rl.Dialogflow API error: {str(e)}"}, status_code=500
        )
    except Exception as e:
        return rl.JSONResponse(
            {"error": f"Internal server error: {str(e)}"}, status_code=500
        )
