from pydantic import BaseModel


class DoctorBase(BaseModel):
    name: str
    specialty: str


class DoctorCreate(DoctorBase):
    pass


class DoctorUpdate(DoctorBase):
    pass


class DoctorRead(DoctorBase):
    id: int

    model_config = {
        "from_attributes": True,
    }
