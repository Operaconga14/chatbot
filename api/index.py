from .config.config import FastAPI, HTTPException, status

app = FastAPI()


#  Testing API
@app.get("/", tags=["Test"], description="Route for testing API")
def read_root():
    return HTTPException(status_code=status.HTTP_200_OK, detail="Welcome to Chatbot")
