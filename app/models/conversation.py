from sqlalchemy import (
    Column, 
    String, 
    Integer, 
    DateTime, 
    CheckConstraint, 
    ForeignKey, 
    UniqueConstraint)

from datetime import datetime
from app.db import Base


class Conversation(Base):
    __tablename__ = "conversation"
    id = Column(Integer, primary_key=True, index=True)
    participant_one_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    participant_two_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)

    __table_args__=(
        UniqueConstraint(
            "participant_one_id",
            "participant_two_id",
            name="uq_dir_conversation_participants"
        ),
        CheckConstraint(
            "participant_one_id < participant_two_id",
            name="ck_dir_conversation_participant"
        ),

    )