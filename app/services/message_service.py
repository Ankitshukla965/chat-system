from datetime import datetime
from app.schemas.message import MessageCreate, MessageResponse


messages = []
message_id_counter = 1


def create_message(message: MessageCreate) -> MessageResponse:
    global message_id_counter

    new_message = MessageResponse(
        id=message_id_counter,
        chat_id=message.chat_id,
        sender_id=message.sender_id,
        content=message.content,
        created_at=datetime.now
    )

    messages.append(new_message)
    message_id_counter += 1

    return new_message

def get_message() -> list[MessageResponse]:
    return messages
