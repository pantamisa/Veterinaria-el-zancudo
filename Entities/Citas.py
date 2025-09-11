"""
Modelo de Citas
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, validator

from database.config import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from uuid import UUID

class Cita(Base):
    __tablename__ = "citas"

    id_cita = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    id_servicio = Column(UUID(as_uuid=True),ForeignKey("servicios.id_servicio"), nullable=False)
    id_animal = Column(UUID(as_uuid=True),ForeignKey("animales.id_animal"), nullable=False)
    fecha_asignacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_atencion = Column(DateTime(timezone=True), nullable=True)

    # Relaciones
    servicio = relationship("Servicio", back_populates="citas")
    animal = relationship("Animal", back_populates="citas")

    def __repr__(self):
        return f"<Cita(id_cita={self.id_cita}, id_servicio={self.id_servicio}, id_animal={self.id_animal})>"


# ======== Esquemas Pydantic ========

class CitaBase(BaseModel):
    id_servicio: uuid.UUID
    id_animal: uuid.UUID
    fecha_asignacion: Optional[datetime] = None
    fecha_atencion: Optional[datetime] = None
    id_usuario_crea: uuid.UUID
    id_usuario_edita: Optional[uuid.UUID] = None

    @validator("id_servicio", "id_animal", "id_usuario_crea")
    def validar_uuid(cls, v):
        if not v:
            raise ValueError("El campo no puede estar vacío")
        return v


class CitaCreate(CitaBase):
    pass


class CitaUpdate(BaseModel):
    fecha_atencion: Optional[datetime] = None
    id_usuario_edita: Optional[uuid.UUID] = None


class CitaResponse(CitaBase):
    id_cita: uuid.UUID
    fecha_creacion: datetime
    fecha_actualizacion: Optional[datetime] = None

    class Config:
        from_attributes = True
