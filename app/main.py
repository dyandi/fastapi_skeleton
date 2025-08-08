from dotenv import load_dotenv  # explicit load .env in local/dev
load_dotenv()

from fastapi import FastAPI
from app.core.config import get_settings
from app.core.logging import setup_logging
from app.api.routers import health, users

setup_logging()
settings = get_settings()

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)
app.include_router(health.router)
app.include_router(users.router)
