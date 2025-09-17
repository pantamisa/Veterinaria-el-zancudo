# models/animal.py
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, CHAR
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field, validator
from typing import Optional
from sqlalchemy.sql import func

from Database.config import Base
 # Asegúrate de que la ruta es correcta


class Animal(Base):
    """
    Modelo de Animal que representa la tabla 'animales'
    """
    __tablename__ = 'animales'

    id_animal = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    id_usuario = Column(UUID(as_uuid=True), ForeignKey('usuarios.id_usuario'))
    nombre_animal = Column(String(200), nullable=False, index=True)
    edad_animal = Column(CHAR(4), nullable=False)
    id_genero = Column(UUID(as_uuid=True), ForeignKey('generos.id_genero'), nullable=False)
    id_raza = Column(UUID(as_uuid=True), ForeignKey('Raza_animal.id_raza'), nullable=False)
    id_usuario_crea = id_usuario = Column(UUID(as_uuid=True), ForeignKey('usuarios.id_usuario'))
    id_usuario_edita = Column(UUID(as_uuid=True), nullable=True, default=None)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())
    # Relaciones

    genero = relationship("Genero", back_populates="animales")
    usuario = relationship("Usuario", back_populates="animales")  # si tienes Usuario
    # raza = relationship("Raza", back_populates="animales")        # si tienes Raza

    def __repr__(self):
        return f"<Animal(id_animal={self.id_animal}, nombre_animal='{self.nombre_animal}')>"


# ======== Esquemas Pydantic ========

class AnimalBase(BaseModel):
    nombre_animal: str = Field(..., min_length=1, max_length=200)
    edad_animal: str = Field(..., min_length=1, max_length=4)
    id_usuario: uuid.UUID
    id_genero: uuid.UUID
    id_raza: uuid.UUID
    id_usuario_crea: uuid.UUID
    id_usuario_edita: Optional[uuid.UUID] = None

    @validator('nombre_animal')
    def validar_nombre(cls, v):
        if not v.strip():
            raise ValueError('El nombre del animal no puede estar vacío')
        return v.strip()

class AnimalCreate(AnimalBase):
    pass

class AnimalUpdate(BaseModel):
    nombre_animal: Optional[str] = Field(None, max_length=200)
    edad_animal: Optional[str] = Field(None, max_length=4)
    id_genero: Optional[uuid.UUID] = None
    id_raza: Optional[uuid.UUID] = None
    id_usuario_edita: Optional[uuid.UUID] = None

    @validator('nombre_animal')
    def validar_nombre(cls, v):
        if v is not None and not v.strip():
            raise ValueError('El nombre del animal no puede estar vacío')
        return v.strip() if v else v

class AnimalResponse(AnimalBase):
    id_animal: uuid.UUID
    fecha_creacion: datetime
    fecha_actualizacion: Optional[datetime] = None

    class Config:
        from_attributes = True
