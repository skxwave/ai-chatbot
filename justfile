infra STATE="up --build -d":
    docker-compose {{STATE}}

dev:
    uv run main.py
