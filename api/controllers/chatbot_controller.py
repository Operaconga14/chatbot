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


def is_valid_session_id(session_id: str | None) -> bool:
    if not session_id or session_id == "string":
        return False
    return session_id.isdigit()


# Start Conversation with Bot
async def start_chat(message, session_id):

    # Dialoflow Calls
    token = scoped_cred.token
    project_id = PROJECT_ID
    url = f"https://dialogflow.googleapis.com/v2/projects/{project_id}/agent/sessions/{session_id}:detectIntent"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {"queryInput": {"text": {"text": message, "languageCode": LANGUAGE_CODE}}}

    dialogflow_res = requests.post(url=url, headers=headers, json=payload)
    dialogflow_res.raise_for_status

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


def close_conversation(payload):
    if not payload or not payload.isdigit():
        return {"message": "Invalid session Id"}
    return {"message": "Conversation closed"}
