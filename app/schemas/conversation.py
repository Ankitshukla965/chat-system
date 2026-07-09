from pydantic import BaseModel
class DirectMessageCreate(BaseModel):
    content: str
    sender_id: int
    recipient_id: int
    