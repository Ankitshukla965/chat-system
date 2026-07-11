from app.db import Base
from datetime import datetime
from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    JSON
)

class MessageEvents(Base):
    __tablename__ = "events"
    id=Column(Integer, primary_key=True, nullable=False, index=True)
    event_type=Column(String, nullable=False, index=True)
    payload=Column(JSON, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.now)
    status = Column(String, nullable=False, index=True)
    retry_count = Column(Integer, nullable=False, index=True, default=0)

