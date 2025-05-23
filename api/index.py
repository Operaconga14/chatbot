from .config.config import FastAPI, HTTPException, status, API_V1

app = FastAPI()


#  Testing API
@app.get(f"{API_V1}", tags=["Test"], description="Route for testing API")
def read_root():
    return HTTPException(status_code=status.HTTP_200_OK, detail="Welcome to Chatbot")
