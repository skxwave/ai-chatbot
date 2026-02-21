from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    db_url: str = "postgresql://postgres:root@localhost:5432/langgraph_store"
    openai_api_key: str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Config()
