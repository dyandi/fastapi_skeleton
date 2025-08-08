from sqlalchemy import String
# noqa: D100
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class Doctor(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    specialty: Mapped[str] = mapped_column(String(255))
