from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    # Base app configuration
    debug: bool = False
    app_name: str = "Langgraph AI chatbot"
    app_version: str = "0.1.0"
    db_url: str = "postgresql://postgres:root@localhost:5432/langgraph_store"
    
    # LLM configuration
    openai_api_key: str
    openai_base_url: str = "https://openrouter.ai/api/v1"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Config()
