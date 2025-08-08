from app.core.config import get_settings
from app.domain.repositories.user_sqlalchemy import UserRepositorySQLAlchemy
from app.domain.services.user_service import UserService

Settings = get_settings

def provide_user_repository(session) -> UserRepositorySQLAlchemy:
    return UserRepositorySQLAlchemy(session=session)

def provide_user_service(session) -> UserService:
    return UserService(repo=provide_user_repository(session))
