from fastapi import APIRouter, Request
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

router = APIRouter()


class ChatRequest(BaseModel):
    message: str = Field(..., example="Tell me about python in 10 words")
    thread_id: str = Field(default="chat_1")
    user_id: str = Field(default="1")


@router.post("/chat")
async def chat(request: Request, body: ChatRequest):
    agent = request.app.state.agent

    config = {
        "configurable": {
            "thread_id": body.thread_id,
            "user_id": body.user_id,
        }
    }

    final_state = await agent.ainvoke(
        {"messages": [HumanMessage(content=body.message)]},
        config=config,
    )

    return {"response": final_state["messages"][-1].content}
