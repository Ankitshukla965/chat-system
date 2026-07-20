from fastapi import APIRouter, HTTPException, Depends, Query
from app.schemas.message import MessageCreate, MessageResponse, MessageListResponse
from app.services import message_service
from sqlalchemy.orm import Session
from app.db import get_db
import logging
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/messages", tags=["Messages"])


@router.post("", response_model=MessageResponse, status_code=201)
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    try:
        return message_service.create_message(message, db)
    except message_service.SameSenderRecipientError:
        raise HTTPException(
            status_code=400,
            detail="sender_id and recipient_id cannot be the same"
        )
    except message_service.MessageParticipantNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Sender or recipient user not found"
        )

@router.get("", response_model=MessageListResponse)
def get_messages(conversation_id: int = Query(gt=0), limit: int = Query(default=20, gt=0, le=100), offset: int = Query(default=0, ge=0), db: Session = Depends(get_db),):
    return message_service.get_message(conversation_id, limit, offset, db)