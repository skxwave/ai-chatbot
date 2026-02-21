from langchain.chat_models import init_chat_model

from src.core.config import settings

model = init_chat_model(
    "openai/gpt-4o-mini",
    model_provider="openai",
    base_url="https://openrouter.ai/api/v1",
    api_key=settings.openai_api_key,
    temperature=0
)
