from datetime import datetime
from app.models.events import MessageEvents
from sqlalchemy import select


def publish_events(db):
    statements = select(MessageEvents).where(MessageEvents.event_type == "pending")
    for statement in statements:
        if statement is not None:
            MessageEvents.status = "processed"
            print("Event Published")
            db.commit(MessageEvents)
            db.refresh(MessageEvents)
            return MessageEvents
        else:
            print("No pending event found")