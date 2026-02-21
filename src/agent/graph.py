from langgraph.graph.state import StateGraph
from langgraph.store.base import BaseStore
from langchain_core.runnables import RunnableConfig

from src.agent.models import model, extraction_llm
from src.agent.states import State
from src.agent.utils import trimmer


async def chat_node(state: State, config: RunnableConfig, store: BaseStore):
    user_id = config["configurable"].get("user_id")
    namespace = ("memories", user_id)

    existing_memory = await store.aget(namespace, "user_profile")
    context = existing_memory.value if existing_memory else "No prior knowledge."

    system_prompt = f"You are a helpful assistant. Known facts about user: {context}"
    messages = [{"role": "system", "content": system_prompt}] + state["messages"][-5:]
    # trimmed_messages = await trimmer.ainvoke(messages)  # Works with specific models

    response = await model.ainvoke(messages, config=config)
    return {"messages": [response]}


async def memory_node(
    state: State,
    config: RunnableConfig,
    store: BaseStore,
):
    user_id = config["configurable"].get("user_id", "default_user")
    if not user_id:
        return state

    namespace = ("memories", user_id)

    # Get 2 last messages: User message & AI message
    last_messages = state["messages"][-2:]

    new_data = await extraction_llm.ainvoke(
        [
            {
                "role": "system",
                "content": "Extract any new permanent user facts from the dialogue. If there is nothing to extract - skip. Return only NEW facts.",
            },
            *last_messages,
        ]
    )
    if new_data.facts:
        existing = await store.aget(namespace, "user_profile")
        old_facts = existing.value.get("facts", []) if existing else []
        
        updated_facts = list(set(old_facts + new_data.facts)) # unique facts
        await store.aput(namespace, "user_profile", {"facts": updated_facts})
    
    return state


def create_graph(
    checkpointer=None,
    store=None,
):
    builder = StateGraph(State)
    builder.add_node("chat", chat_node)
    builder.add_node("update_memory", memory_node)

    builder.set_entry_point("chat")
    builder.add_edge("chat", "update_memory")
    builder.set_finish_point("update_memory")

    return builder.compile(
        checkpointer=checkpointer,
        store=store,
    )


# For langgraph.json
graph = create_graph()
