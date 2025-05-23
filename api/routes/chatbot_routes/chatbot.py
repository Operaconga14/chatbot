from ...config.config import APIRouter, HTTPException, status, Response, Request
from ...controllers.chatbot_controller import generate_session_id, start_chat


router = APIRouter(tags=["ChatBot"])


@router.get("/", summary="Route for testing chatbot api route")
def read_chatbot():
    return HTTPException(
        status_code=status.HTTP_200_OK, detail="Chatbot api route is working"
    )


@router.post("/conversation")
async def start_conversation(response: Response):
    conversation = await start_chat(response=response)
    return conversation
