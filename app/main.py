from fastapi import FastAPI
from app.db import Base, engine
from app.models.message import Message
from app.api.health import router as health_router
from app.api.users import router as users_router
from app.api.messages import router as message_router

app = FastAPI(title="Chat System API")

Base.metadata.create_all(bind=engine)

app.include_router(health_router)
app.include_router(users_router)
app.include_router(message_router)