from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field

from src.core.config import settings


class UserFacts(BaseModel):
    facts: list[str] = Field(description="List of facts about user.")


model = init_chat_model(
    "openai/gpt-4o-mini",
    model_provider="openai",
    base_url="https://openrouter.ai/api/v1",
    api_key=settings.openai_api_key,
    temperature=0
)
extraction_llm = model.with_structured_output(UserFacts)
