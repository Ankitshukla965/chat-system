from datetime import datetime
from pydantic import BaseModel, ConfigDict


class MessageCreate(BaseModel):
    chat_id: int
    sender_id: int
    content: str


class MessageResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    chat_id: int
    sender_id: int
    content: str
    created_at: datetime