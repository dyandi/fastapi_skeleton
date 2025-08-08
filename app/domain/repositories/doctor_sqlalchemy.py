from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.models.doctor import Doctor


class DoctorRepositorySQLAlchemy:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, *, name: str, specialty: str) -> Doctor:
        doctor = Doctor(name=name, specialty=specialty)
        self.session.add(doctor)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise
        await self.session.refresh(doctor)
        return doctor

    async def get_by_id(self, doctor_id: int):
        res = await self.session.execute(select(Doctor).where(Doctor.id == doctor_id))
        return res.scalar_one_or_none()

    async def update(self, doctor_id: int, *, name: str, specialty: str):
        res = await self.session.execute(select(Doctor).where(Doctor.id == doctor_id))
        doctor = res.scalar_one_or_none()
        if not doctor:
            return None
        doctor.name = name
        doctor.specialty = specialty
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise
        await self.session.refresh(doctor)
        return doctor

    async def delete(self, doctor_id: int):
        res = await self.session.execute(select(Doctor).where(Doctor.id == doctor_id))
        doctor = res.scalar_one_or_none()
        if not doctor:
            return
        await self.session.delete(doctor)
        try:
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise
