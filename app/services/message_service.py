from datetime import datetime
from app.schemas.message import MessageCreate, MessageResponse
from sqlalchemy.orm import Session
from app.models.message import Message
from fastapi import Query
from sqlalchemy import select





def create_message(message: MessageCreate, db: Session):
    

    db_message = Message(
        
        
        sender_id=message.sender_id,
        recipient_id=message.recipient_id,
        content=message.content,
     
    )
    
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
 
    return db_message

def get_message(chat_id, db) -> list[Message]:
    statement = (
    select(Message)
    .where(Message.chat_id == chat_id)
    .order_by(Message.created_at)
)
    messages = db.scalars(statement).all()
    return messages
