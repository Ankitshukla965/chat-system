from datetime import datetime
from app.models.events import MessageEvents
from sqlalchemy import select
from app.enum import EventStatus, EventType


def process_next_event(db):
    statements = (select(MessageEvents)
    .where(MessageEvents.status == EventStatus.PENDING.value)
    .order_by(MessageEvents.created_at))
    event = db.scalars(statements).first()
    if event is not None:
            event.status = EventStatus.PROCESSING.value
            db.commit()
            try:
                event.status = EventStatus.PROCESSED.value
                print("Event Published")
                db.commit()
                db.refresh(event)
            except Exception as error:
                print(str(error))
                
                event.status =   EventStatus.FAILED.value
                event.retry_count += 1
                db.commit()
            return event
    else:
        print("No pending event found")
        return None

def process_all_pending_events(db):
   
    while True:
        event = process_next_event(db)
        if event is None:
             break
        processed_count += 1
    return processed_count

        