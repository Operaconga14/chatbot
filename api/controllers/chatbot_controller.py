from ..config.config import uuid, Response, Request

# Generate Session Id
def generate_session_id():
    session_id = str(uuid.uuid4().int)[:6]
    return session_id

# Store Session Id
def store_id(response: Response, session_id):
    response.set_cookie("session_id", session_id)

# Start Conversation with Bot
async def start_chat(response: Response):
    session_id = generate_session_id()
    store_id(response=response, session_id=session_id)
    print("SessionId", session_id)
    return {"sessionId": session_id}
