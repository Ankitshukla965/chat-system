from datetime import datetime
from app.schemas.message import MessageCreate, MessageResponse
from sqlalchemy.orm import Session
from app.models.message import Message
from fastapi import Query
from sqlalchemy import select

conversation_id = 1



def create_message(message: MessageCreate, db: Session):
    

    db_message = Message(
        
        conversation_id=conversation_id,
        sender_id=message.sender_id,
        receiver_id=message.receiver_id,
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
