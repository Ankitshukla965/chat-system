from fastapi import APIRouter, HTTPException
from app.schemas.message import MessageCreate, MessageResponse
from app.services import message_service

router = APIRouter(prefix="/messages", tags=["Messages"])


@router.post("", response_model=MessageResponse, status_code=201)
def create_message(message: MessageCreate):
    return message_service.create_message(message)