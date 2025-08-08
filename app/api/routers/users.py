from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_session
from app.core.container import provide_user_service
from app.domain.schemas.user import UserCreate, UserRead

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(payload: UserCreate, session: AsyncSession = Depends(get_session)):
    service = provide_user_service(session)
    try:
        return await service.register(payload)
    except Exception:
        raise HTTPException(status_code=400, detail="cannot create user")

@router.get("/{user_id}", response_model=UserRead)
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    service = provide_user_service(session)
    user = await service.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user
