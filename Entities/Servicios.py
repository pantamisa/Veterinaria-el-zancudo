"""
Modelo de Servicios
"""

import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, validator

from database.config import Base
from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from uuid import UUID

class Servicio(Base):
    __tablename__ = "servicios"

    id_servicio = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    nombre_ser = Column(String(100), nullable=False)
    costo = Column(Float, nullable=False)
   
    # Relación con Citas (un servicio puede tener muchas citas)
    citas = relationship("Cita", back_populates="servicio")

    def __repr__(self):
        return f"<Servicio(id_servicio={self.id_servicio}, nombre_ser='{self.nombre_ser}', costo={self.costo})>"


# ======== Esquemas Pydantic ========

class ServicioBase(BaseModel):
    nombre_ser: str = Field(..., min_length=1, max_length=100)
    costo: float
    id_usuario_crea: uuid.UUID
    id_usuario_edita: Optional[uuid.UUID] = None

    @validator("nombre_ser")
    def validar_nombre(cls, v):
        if not v.strip():
            raise ValueError("El nombre del servicio no puede estar vacío")
        return v.strip()


class ServicioCreate(ServicioBase):
    pass


class ServicioUpdate(BaseModel):
    nombre_ser: Optional[str] = Field(None, max_length=100)
    costo: Optional[float] = None
    id_usuario_edita: Optional[uuid.UUID] = None

    @validator("nombre_ser")
    def validar_nombre(cls, v):
        if v is not None and not v.strip():
            raise ValueError("El nombre del servicio no puede estar vacío")
        return v.strip() if v else v


class ServicioResponse(ServicioBase):
    id_servicio: uuid.UUID
 

    class Config:
        from_attributes = True
