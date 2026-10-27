from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings. Values come from environment variables and the .env file."""

    model_config = SettingsConfigDict(env_file="../.env", extra="ignore")

    database_url: str = "postgresql+psycopg://docchat:docchat@localhost:5432/docchat"
    openai_api_key: str = ""
    chat_model: str = "gpt-5.4-mini"
    embedding_model: str = "text-embedding-3-small"


settings = Settings()
