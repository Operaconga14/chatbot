from ...config.config import APIRouter, HTTPException, status

router = APIRouter(tags=["ChatBot"])


@router.get("/", summary="Route for testing chatbot api route")
def read_chatbot():
    return HTTPException(
        status_code=status.HTTP_200_OK, detail="Chatbot api route is working"
    )


@router.post("/conversation")
def start_conversation():
    pass
