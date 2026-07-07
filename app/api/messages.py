from fastapi import APIRouter, HTTPException, Depends
from app.schemas.message import MessageCreate, MessageResponse
from app.services import message_service
from sqlalchemy.orm import Session
from app.db import get_db

router = APIRouter(prefix="/messages", tags=["Messages"])


@router.post("", response_model=MessageResponse, status_code=201)
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    return message_service.create_message(message, db)

@router.get("", response_model=list[MessageResponse])
def get_messages():
    return message_service.get_messages()