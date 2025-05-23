from ..config.config import (
    uuid,
    Request,
    JSONResponse,
    dialogflow,
    LANGUAGE_CODE,
    PROJECT_ID,
    GoogleAPICallError,
    session_client
)


def generate_session_id():
    session_id = str(uuid.uuid4().hex)[:6]
    return session_id


async def start_conversation(request: Request, message):
    try:
        # Get user message from request

        user_message = message.message

        if not user_message:
            return JSONResponse({"error": "No message provided"}, status_code=400)

        # Generate or get session ID
        session_id = request.cookies.get("session_id")
        if not session_id:
            session_id = generate_session_id()

        # Create session path
        session = session_client.session_path(PROJECT_ID, session_id)

        text_input = dialogflow.TextInput(
            text=user_message,
            language_code=LANGUAGE_CODE,
        )

        query_input = dialogflow.QueryInput(text=text_input)

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
        res = JSONResponse(content=response_data, status_code=200)
        res.set_cookie(key="session_id", value=session_id)

        return res
    except GoogleAPICallError as e:
        return JSONResponse(
            {"error": f"Dialogflow API error: {str(e)}"}, status_code=500
        )

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
