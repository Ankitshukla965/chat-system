from pydantic import BaseModel
class DirectMessageCreate(BaseModel):
    content: str
    sender_id: id
    reciever_id: id
    