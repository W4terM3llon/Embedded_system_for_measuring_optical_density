docker build -f ".\dockerfile.server" . -t yeast_server

docker build -f ".\dockerfile.client" . -t yeast_client

docker compose up -d