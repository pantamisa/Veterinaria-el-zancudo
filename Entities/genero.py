# models/genero.py
import uuid 
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field, validator
from sqlalchemy.sql import func
from datetime import datetime

from Database.config import Base
 # Ajusta a tu ruta real


class Genero(Base):
    """
    Modelo de Genero que representa la tabla 'generos'
    """
    __tablename__ = 'generos'

    id_genero = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    nombre_genero = Column(String(10), nullable=False, index=True)

    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())
    # Relación inversa para ver animales de este género
    animales = relationship("Animal", back_populates="genero")

    def __repr__(self):
        return f"<Genero(id_genero={self.id_genero}, nombre_genero='{self.nombre_genero}')>"


# ======== Esquemas Pydantic ========

class GeneroBase(BaseModel):
    nombre_genero: str = Field(..., min_length=1, max_length=10, description="Nombre del género")

    @validator('nombre_genero')
    def validar_nombre(cls, v):
        if not v.strip():
            raise ValueError('El nombre del género no puede estar vacío')
        return v.strip()

class GeneroCreate(GeneroBase):
    pass

class GeneroResponse(GeneroBase):
    id_genero: uuid.UUID

    class Config:
        from_attributes = True
