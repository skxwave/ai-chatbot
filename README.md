# AI Chatbot

Chatbot built using LangGraph and LangChain with support for short-term and long-term memory.

Features
- LangGraph orchestration for composing multi-step agent logic
- LangChain integration for LLM access and chains
- Chatbot memory with PostgreSQL for conversational context in one chat and between them

Quickstart
1. Create and activate a virtual environment:

```bash
python -m venv .venv
# Or using UV:
uv venv .venv

# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

2. Install dependencies:

```bash
uv sync
```

3. Fill environment variables:
```bash
cp .env.template .env
```

4. Run the infrastructure:
```bash
docker-compose up --build -d
# Or using `justfile`
just infra
```

5. Run the chatbot:

```bash
uv run main.py
# Or using `justfile`:
just dev
```

Notes
- API implementation: [src/api/chatbot.py](src/api/chatbot.py)
- Agent logic and graph orchestration: [src/agent/graph.py](src/agent/graph.py)
- Configuration: [src/core/config.py](src/core/config.py)

Contributing
- Feel free to open issues or pull requests. Keep changes focused and include tests when possible.

License
- See the project LICENSE file.


