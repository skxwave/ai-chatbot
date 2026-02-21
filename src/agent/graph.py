from langgraph.graph.state import StateGraph
from langchain_core.runnables import RunnableConfig

from src.agent.models import model
from src.agent.states import State


async def chat_node(
    state: State,
    config: RunnableConfig,
):
    messages = state["messages"]
    response = await model.ainvoke(messages, config=config)
    return {"messages": [response]}


def create_graph(checkpointer=None):
    builder = StateGraph(State)
    builder.add_node("chat", chat_node)
    builder.set_entry_point("chat")
    builder.set_finish_point("chat")
    return builder.compile(checkpointer=checkpointer)


# For langgraph.json
graph = create_graph()
