from ...config.config import APIRouter, HTTPException, status, Response, Request
from ...controllers.chatbot_controller import (
    generate_session_id,
    start_chat,
    close_conversation,
    is_valid_session_id,
)
from ...models.schemas import ChatRequest, CloseRequest


router = APIRouter(tags=["ChatBot"])


@router.get("/", summary="Route for testing chatbot api route")
def read_chatbot():
    return HTTPException(
        status_code=status.HTTP_200_OK, detail="Chatbot api route is working"
    )


@router.post("/conversation", summary="Route for conversation with bot")
async def start_conversation(message: ChatRequest):
    if not is_valid_session_id(message.session_id):
        session_id = generate_session_id()
    else:
        session_id = message.session_id

    conversation = await start_chat(message=message.message, session_id=session_id)
    return conversation


@router.post("/end", summary="Route to end conversation End and to delete chat traces")
async def end_conversation(payload: CloseRequest):
    conversation_end = close_conversation(payload=payload.session_id)
    return conversation_end
