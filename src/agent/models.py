from langchain.chat_models import init_chat_model

from src.core.config import settings
from .schemas import UserFacts


# Base chat LLM
llm = init_chat_model(
    "openai/gpt-4o-mini",
    model_provider="openai",
    base_url=settings.openai_base_url,
    api_key=settings.openai_api_key,
    temperature=0,
)

# LLM for extracting user facts for long-term memory
extraction_llm = llm.with_structured_output(UserFacts)
