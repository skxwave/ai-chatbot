from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(..., example="Tell me about python in 10 words")
    thread_id: str = Field(default="chat_1")
    user_id: str = Field(default="1")
