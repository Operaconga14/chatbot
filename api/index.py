from api.config.config import rl
from api.controller.chat_controller import generate_chat_id, start_chat, test_url


app = rl.FastAPI(title="Chatbot API", version="1.0.0", summary="Chat bot API")

app.add_middleware(
    rl.CORSMiddleware,
    allow_origins=rl.origins,  # or ["*"] to allow all origins (not recommended for prod)
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # allowed HTTP methods
    allow_headers=["*"],  # allowed headers
)


class ChatRquest(rl.BaseModel):
    message: str


#  Testing API
@app.get(f"{rl.API_V1}", tags=["Test"], description="Route for testing API")
def read_root():
    return rl.HTTPException(
        status_code=rl.status.HTTP_200_OK, detail="Welcome to Chatbot"
    )


# Chat Id
@app.get(
    f"{rl.API_V1}/generate", tags=["Chatbot"], description="Generate Chat Id on load"
)
async def chat_id_geerate():
    chat_id = generate_chat_id()
    print("Chat Id", chat_id)
    return {"chat_id": chat_id}


@app.post(f"{rl.API_V1}/chat", tags=["Chatbot"], description="Conversation API")
async def chat():
    response = test_url()
    print("Resp", response)
    return {"response": response}
