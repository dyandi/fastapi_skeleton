.PHONY: run dev fmt lint test migrate revision

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

dev:
	pre-commit install

fmt:
	ruff check --fix .

lint:
	ruff check . && mypy app

test:
	pytest -q

revision:
	alembic revision -m "init"

migrate:
	alembic upgrade head
