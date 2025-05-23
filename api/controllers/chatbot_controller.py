from ..config.config import uuid, Response, Request


# Generate Session Id
def generate_session_id():
    session_id = str(uuid.uuid4().int)[:6]
    return session_id


# Store Session Id
def store_id(response: Response, session_id):
    response.set_cookie("session_id", session_id)


# Start Conversation with Bot
async def start_chat(response: Response, message, request: Request):
    # get the Generated Session Id
    session_id = request.cookies.get("session_id")

    if session_id is None:
        session_id = generate_session_id()
        store_id(response=response, session_id=session_id)
        return {"message": f"{session_id} is stored succesfully"}

    return {"sessionId": session_id}


def close_conversation(request: Request):
    # clear all Session Id
    session_id = request.cookies.get("session_id")

    if session_id is None:
        return {"message": "No active conversation"}

    response = Response(
        content='{"message": "conversation closed"}', media_type="application/json"
    )
    response.delete_cookie("session_id")

    return response
