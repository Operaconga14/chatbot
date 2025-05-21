from api.config.config import rl, get_context
from api.controller.chat_controller import generate_chat_id, start_chat, test_url


class NoCacheStaticFiles(rl.StaticFiles):
    async def get_response(self, path: str, scope):
        response = await super().get_response(path, scope)
        # Set headers to prevent caching
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response


app = rl.FastAPI(title="Chatbot API")
app.add_middleware(
    rl.CORSMiddleware,
    allow_origins=rl.origins,  # or ["*"] to allow all origins (not recommended for prod)
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # allowed HTTP methods
    allow_headers=["*"],  # allowed headers
)
templates = rl.Jinja2Templates(directory="templates")
app.mount("/static", rl.StaticFiles(directory="static"), name="static")


class ChatRquest(rl.BaseModel):
    message: str


# Home interface
@app.get(f"/", response_class=rl.HTMLResponse)
def index(request: rl.Request):
    return templates.TemplateResponse("index.html", get_context(request=request))


# Chat Id
@app.get(f"{rl.API_V1}/generate")
async def chat_id_geerate():
    chat_id = generate_chat_id()
    print("Chat Id", chat_id)
    return {"chat_id": chat_id}


# Chat
# @app.post("/chat")
# async def chat(request: ChatRquest):
#     response = start_chat(message=request.message)
#     print("Message", response)
#     return {"response": response}


@app.post(f"{rl.API_V1}/chat")
async def chat():
    response = test_url()
    print("Resp", response)
    return {"response": response}
