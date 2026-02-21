from fastapi import APIRouter, Request
from langchain_core.messages import HumanMessage

from .schemas import ChatRequest

router = APIRouter()


@router.post("/chat/invoke")
async def chat(
    request: Request,
    body: ChatRequest,
):
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
