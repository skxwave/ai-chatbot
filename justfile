infra STATE="up --build -d":
    docker-compose {{STATE}} db pgadmin

docker STATE="up --build -d":
    docker-compose {{STATE}}

dev:
    uv run main.py
