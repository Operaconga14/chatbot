from .config.config import (
    origins,
    FastAPI,
    Response,
    API_V1,
    HTTPException,
    status,
    Request,
)
from .models.schemas import ChatRequest
from .controllers.chatbot_controller import generate_session_id, start_conversation

app = FastAPI()


#  Testing API
@app.get(f"{API_V1}", tags=["Test"], description="Route for testing API")
def read_root():
    return HTTPException(status_code=status.HTTP_200_OK, detail="Welcome to Chatbot")


# Chat Id
@app.post(
    f"{API_V1}/chat",
    tags=["Chatbot"],
    description="Conversation API first generating session id (chat_id)",
)
async def chat(response: Response):
    # Generate SessionId
    session_id = generate_session_id()
    # print("Session Id :", session_id)

    # store the session id into cookies
    response.set_cookie("session_id", session_id)
    return session_id


# Conversation responder
@app.post(
    f"{API_V1}/chat/conversation",
    tags=["Chatbot"],
    description="Conversational chat with chatobt",
)
async def conversational_chat(chat_request: ChatRequest, request: Request):
    conversation = await start_conversation(message=chat_request, request=request)
    return conversation
