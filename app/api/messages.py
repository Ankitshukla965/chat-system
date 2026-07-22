from fastapi import APIRouter, HTTPException, Depends, Query
from app.schemas.message import MessageCreate, MessageResponse, MessageListResponse
from app.services import message_service
from sqlalchemy.orm import Session
from app.db import get_db
import logging
from app.error import api_error
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/messages", tags=["Messages"])


@router.post("", response_model=MessageResponse, status_code=201)
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    try:
        return message_service.create_message(message, db)
    except message_service.SameSenderRecipientError:
       
        raise HTTPException(
            status_code=400,
            detail= api_error("SAME_SENDER_RECIPIENT_ERROR", "Same Sender and Recipient Error", None)
        
        )
    except message_service.MessageParticipantNotFoundError:
        raise HTTPException(
            status_code=404,
            detail=api_error("MESSAGE_PARTCIPANTS_NOT_FOUND", "Message Participants Not Found", "None")
        )

@router.get("", response_model=MessageListResponse)
def get_messages(conversation_id: int = Query(gt=0), limit: int = Query(default=20, gt=0, le=100), offset: int = Query(default=0, ge=0), db: Session = Depends(get_db),):
    return message_service.get_message(conversation_id, limit, offset, db)