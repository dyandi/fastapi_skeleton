# FastAPI Skeleton (SOLID)

## Quickstart
```bash
cp .env.example .env
# edit .env if needed
pip install -e .[dev]
make run
# or using docker
docker compose up --build
```

## Endpoints
- `GET /healthz`
- `POST /users` {email, full_name, password}
- `GET /users/{id}`
