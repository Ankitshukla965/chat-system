from datetime import datetime
from app.schemas.message import MessageCreate, MessageResponse
from sqlalchemy.orm import Session
from app.models.message import Message
from app.models.conversation import Conversation
from fastapi import Query
from sqlalchemy import select


class SameSenderRecipientError(Exception):
    pass

   
def create_message(message: MessageCreate, db: Session):
     
    sender_id=message.sender_id
    recipient_id=message.recipient_id
    
    if(sender_id==recipient_id):
        raise SameSenderRecipientError()
    
    participant_one_id = min(sender_id,recipient_id)
    participant_two_id = max(sender_id,recipient_id)
      
    statement = select(Conversation).where(
    Conversation.participant_one_id == participant_one_id,
    Conversation.participant_two_id == participant_two_id,
    )
    
    conversation = db.scalars(statement).first()

    if conversation is None:
    
        db_conversation = Conversation(
            participant_one_id=participant_one_id,
            participant_two_id=participant_two_id,
            
        )

        db.add(db_conversation)
        db.flush()
        conversation=db_conversation
   

    db_message = Message(
        sender_id=message.sender_id,
        conversation_id=conversation.id,
        content=message.content
    )

    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message
                

def get_message(conversation_id, db) -> list[Message]:
    statement = (
    select(Message)
    .where(Message.chat_id == conversation_id)
    .order_by(Message.created_at)
)
    messages = db.scalars(statement).all()
    return messages



