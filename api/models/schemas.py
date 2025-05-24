from ..config.config import BaseModel, Optional


class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None


class CloseRequest(BaseModel):
    session_id: str
