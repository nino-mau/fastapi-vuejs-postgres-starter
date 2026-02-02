from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "My App"
    admin_email: str = "admin@app.com"
    database_url: str = ""  # Value read from .env


settings = Settings()
