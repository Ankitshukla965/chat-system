from enum import Enum

class EventStatus(Enum):
    PENDING = "pending"
    PROCESSED = "processed"
    PROCESSING = "processing"
    FAILED = "failed"

class EventType(Enum):
    MESSAGESENT = "message_sent"
    

