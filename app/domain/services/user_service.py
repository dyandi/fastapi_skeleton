from typing import Optional
from app.domain.schemas.user import UserCreate, UserRead
from app.domain.repositories.base import UserRepository
from app.utils.security import get_password_hash

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def register(self, payload: UserCreate) -> UserRead:
        hashed = get_password_hash(payload.password)
        user = await self.repo.create(
            email=payload.email,
            full_name=payload.full_name,
            hashed_password=hashed,
        )
        return UserRead.model_validate(user)

    async def get(self, user_id: int) -> Optional[UserRead]:
        user = await self.repo.get_by_id(user_id)
        return UserRead.model_validate(user) if user else None
