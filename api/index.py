from .config.config import FastAPI, HTTPException, status, API_V1
from .routes.chatbot_routes import chatbot

app = FastAPI(
    title="Chat Bot API",
    description="Chatbot API swagger documentation and testing",
    version="1.0.0",
)


#  Testing API
@app.get(f"/{API_V1}", tags=["Test"], description="Route for testing API")
def read_root():
    return HTTPException(status_code=status.HTTP_200_OK, detail="Welcome to Chatbot")


# Other Routes
app.include_router(chatbot.router, prefix=f"/{API_V1}/chat")
