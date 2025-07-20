from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings from environment variables."""

    app_name: str = "Subscription Service Backend"
    environment: str = "development"
    debug: bool = False
    log_level: str = "INFO"
    log_file: str = "flask_app.log"  # This will be replaced by a more appropriate name later
    redis_url: str = "redis://localhost:6379/0"
    cors_origins: list[str] = ["http://localhost:3000"]  # Example: adjust for production

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
