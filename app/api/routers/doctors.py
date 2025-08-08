from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_session
from app.core.container import provide_doctor_service
from app.domain.schemas.doctor import DoctorCreate, DoctorRead, DoctorUpdate

router = APIRouter(prefix="/doctors", tags=["doctors"])


@router.post("/", response_model=DoctorRead, status_code=status.HTTP_201_CREATED)
async def create_doctor(
    payload: DoctorCreate, session: AsyncSession = Depends(get_session)
):
    service = provide_doctor_service(session)
    try:
        return await service.create(payload)
    except Exception:
        raise HTTPException(status_code=400, detail="cannot create doctor")


@router.get("/{doctor_id}", response_model=DoctorRead)
async def get_doctor(doctor_id: int, session: AsyncSession = Depends(get_session)):
    service = provide_doctor_service(session)
    doctor = await service.get(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="doctor not found")
    return doctor


@router.put("/{doctor_id}", response_model=DoctorRead)
async def update_doctor(
    doctor_id: int,
    payload: DoctorUpdate,
    session: AsyncSession = Depends(get_session),
):
    service = provide_doctor_service(session)
    doctor = await service.update(doctor_id, payload)
    if not doctor:
        raise HTTPException(status_code=404, detail="doctor not found")
    return doctor


@router.delete("/{doctor_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_doctor(doctor_id: int, session: AsyncSession = Depends(get_session)):
    service = provide_doctor_service(session)
    await service.delete(doctor_id)
