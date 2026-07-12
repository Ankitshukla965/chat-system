from datetime import datetime
from app.schemas.message import MessageCreate, MessageResponse
from sqlalchemy.orm import Session
from app.models.message import Message
from app.models.conversation import Conversation
from app.models.events import MessageEvents
from fastapi import Query
from sqlalchemy import select
from app.models.user import User
from app.enum import EventStatus, EventType


class SameSenderRecipientError(Exception):
    pass

class MessageParticipantNotFoundError(Exception):
    pass
   
def create_message(message: MessageCreate, db: Session):
     
    sender_id=message.sender_id
    recipient_id=message.recipient_id
    
    if(sender_id==recipient_id):
        raise SameSenderRecipientError()

    sender = db.get(User, sender_id)
    recipient = db.get(User, recipient_id)

    if sender is None or recipient is None:
        raise MessageParticipantNotFoundError()


   
    
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
    db.flush()
    
    
    event_payload = {
        "message_id": db_message.id,
        "conversation_id": conversation.id,
        "sender_id": sender_id,
        "recipient_id": recipient_id
    }

    event = MessageEvents(
        event_type= EventType.MESSAGESENT.value,
        status=EventStatus.PENDING.value,
        payload=event_payload

    )
    db.add(event)
    db.commit()
    db.refresh(event)
    
    return db_message
              

def get_message(conversation_id, db) -> list[Message]:
    statement = (
    select(Message)
    .where(Message.conversation_id == conversation_id)
    .order_by(Message.created_at)
)
    messages = db.scalars(statement).all()
    return messages



