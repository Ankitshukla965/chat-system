from datetime import datetime
from app.schemas.message import MessageCreate, MessageResponse
from sqlalchemy.orm import Session
from app.models.message import Message


messages = []
message_id_counter = 1


def create_message(message: MessageCreate, db: Session):
  

    db_message = Message(
        
        chat_id=message.chat_id,
        sender_id=message.sender_id,
        content=message.content,
     
    )
    
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
 
    return db_message

def get_message() -> list[MessageResponse]:
    return messages
