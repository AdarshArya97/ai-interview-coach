from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = ""
    gemini_api_key: str = ""
    gemini_model: str = "gemini-3.8-flash"
    llm_timeout_seconds: float = 60.0
    embedding_model: str = "gemini-embedding-001"
    embedding_dimensions: int = 768

settings = Settings()