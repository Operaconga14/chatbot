from .config.config import (
    origins,
    FastAPI,
    Response,
    API_V1,
    HTTPException,
    status,
    Request,
)

app = FastAPI()


#  Testing API
@app.get(f"{API_V1}", tags=["Test"], description="Route for testing API")
def read_root():
    return HTTPException(status_code=status.HTTP_200_OK, detail="Welcome to Chatbot")