from pydantic import BaseModel, Field


class UserFacts(BaseModel):
    facts: list[str] = Field(description="List of facts about user.")
