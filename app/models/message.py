from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    coversation_id = Column(Integer, index=True)
    sender_id = Column(Integer, index=True)
    receiver_id = Column(Integer, index=True)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())