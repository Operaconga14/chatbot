from ..config.config import (
    uuid,
    Response,
    Request,
    scoped_cred,
    PROJECT_ID,
    LANGUAGE_CODE,
    requests,
    JSONResponse,
)


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

    # Dialoflow Calls
    token = scoped_cred.token

    project_id = f"{PROJECT_ID}"

    url = f"https://dialogflow.googleapis.com/v2/projects/{project_id}/agent/sessions/{session_id}:detectIntent"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {"queryInput": {"text": {"text": message, "languageCode": LANGUAGE_CODE}}}

    dialogflow_res = requests.post(url=url, headers=headers, json=payload)
    dialogflow_res.raise_for_status()

    result = dialogflow_res.json()
    fulfilment_text = result["queryResult"]["fulfillmentText"]
    intent_name = result["queryResult"]["intent"]["displayName"]

    response_data = {
        "session_id": session_id,
        "user_message": message,
        "bot_response": fulfilment_text,
        "detected_intent": intent_name,
    }

    res = JSONResponse(content=response_data, status_code=200)
    res.set_cookie(key="session_id", value=session_id)
    return res


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
