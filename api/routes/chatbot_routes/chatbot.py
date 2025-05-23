from ...config.config import APIRouter, HTTPException, status, Response, Request
from ...controllers.chatbot_controller import (
    generate_session_id,
    start_chat,
    close_conversation,
)
from ...models.schemas import ChatRequest


router = APIRouter(tags=["ChatBot"])


@router.get("/", summary="Route for testing chatbot api route")
def read_chatbot():
    return HTTPException(
        status_code=status.HTTP_200_OK, detail="Chatbot api route is working"
    )


@router.post("/conversation", summary="Route for conversation with bot")
async def start_conversation(
    response: Response, request: Request, message: ChatRequest
):
    user_message = message.message
    conversation = await start_chat(
        response=response, request=request, message=user_message
    )
    return conversation


@router.post("/end", summary="Route to end conversation End and to delete chat traces")
async def end_conversation(request: Request):
    conversation_end = close_conversation(request=request)
    return conversation_end
