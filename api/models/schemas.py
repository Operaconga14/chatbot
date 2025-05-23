from ..config.config import BaseModel


class ChatRequest(BaseModel):
    message: str
