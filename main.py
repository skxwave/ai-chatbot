import asyncio
from contextlib import asynccontextmanager
import sys

import uvicorn
from fastapi import FastAPI
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from langgraph.store.postgres.aio import AsyncPostgresStore
from psycopg_pool import AsyncConnectionPool

from src.api.chatbot import router as chat_router
from src.agent.graph import create_graph
from src.core.config import settings

# For windows
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

connection_kwargs = {
    "autocommit": True,
    "prepare_threshold": 0,
}


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with AsyncConnectionPool(
        settings.db_url,
        kwargs=connection_kwargs,
    ) as pool:
        checkpointer = AsyncPostgresSaver(pool)
        await checkpointer.setup()

        store = AsyncPostgresStore(pool)
        await store.setup()

        app.state.agent = create_graph(
            checkpointer=checkpointer,
            store=store,
        )

        yield


app = FastAPI(lifespan=lifespan)
app.include_router(chat_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1", 
        port=8000, 
        loop="asyncio",
        reload=True
    )
