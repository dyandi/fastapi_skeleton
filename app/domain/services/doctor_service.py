from typing import Optional
from app.domain.schemas.doctor import DoctorCreate, DoctorRead, DoctorUpdate
from app.domain.repositories.base import DoctorRepository


class DoctorService:
    def __init__(self, repo: DoctorRepository):
        self.repo = repo

    async def create(self, payload: DoctorCreate) -> DoctorRead:
        doctor = await self.repo.create(name=payload.name, specialty=payload.specialty)
        return DoctorRead.model_validate(doctor)

    async def get(self, doctor_id: int) -> Optional[DoctorRead]:
        doctor = await self.repo.get_by_id(doctor_id)
        return DoctorRead.model_validate(doctor) if doctor else None

    async def update(self, doctor_id: int, payload: DoctorUpdate) -> Optional[DoctorRead]:
        doctor = await self.repo.update(
            doctor_id, name=payload.name, specialty=payload.specialty
        )
        return DoctorRead.model_validate(doctor) if doctor else None

    async def delete(self, doctor_id: int) -> None:
        await self.repo.delete(doctor_id)
