from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Chat System AI"
    event_max_retries : int = 3
    event_batch_size : int = 3
    10

settings = Settings()
