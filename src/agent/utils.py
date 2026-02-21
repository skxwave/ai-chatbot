from langchain_core.messages import trim_messages

from src.agent.models import llm

trimmer = trim_messages(
    max_tokens=4000,
    strategy="last",
    token_counter=llm,
    include_system=True,
    allow_partial=False,
)
