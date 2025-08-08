from app.core.config import get_settings
from app.domain.repositories.user_sqlalchemy import UserRepositorySQLAlchemy
from app.domain.repositories.doctor_sqlalchemy import DoctorRepositorySQLAlchemy
from app.domain.services.user_service import UserService
from app.domain.services.doctor_service import DoctorService

Settings = get_settings

def provide_user_repository(session) -> UserRepositorySQLAlchemy:
    return UserRepositorySQLAlchemy(session=session)

def provide_user_service(session) -> UserService:
    return UserService(repo=provide_user_repository(session))


def provide_doctor_repository(session) -> DoctorRepositorySQLAlchemy:
    return DoctorRepositorySQLAlchemy(session=session)


def provide_doctor_service(session) -> DoctorService:
    return DoctorService(repo=provide_doctor_repository(session))
