from fastapi import FastAPI, Depends
from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.db import get_db
from app.services import event_services

router = APIRouter(prefix="/events", tags=["events"])

@router.post("/", status_code=201)
def publish_event(db: Session=Depends(get_db)):
    return event_services.process_next_event(db)