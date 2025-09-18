from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship
from pydantic import BaseModel, EmailStr, Field, validator
from datetime import datetime
from typing import Optional, List

from database.config import Base
import uuid
from uuid import UUID

class Raza_animal(Base):
    """
    Modelo de Raza_animal que representa la tabla 'Raza_animal'
    
    Atributos:
        id_raza: Identificador único de cada raza de animal
        nombreRaza: Nombre de la raza del animal (único)
        id_tipoAnimal: tipo de animal al que pertenece la raza (clave foranea)
    """
    
    __tablename__ = 'Raza_animal'
    id_raza = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombreRaza = Column(String(100), nullable=False)
    id_tipoAnimal=Column(Integer, ForeignKey('Tipo_animal.id_tipoAnimal'), nullable=False, autoincrement=True)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

    # Claves foráneas
    id_tipoAnimal = Column(
        UUID(as_uuid=True), ForeignKey("Tipo_animal.id_tipoAnimal"), nullable=False
    )

    # Campos de auditoría
    id_usuario_crea = Column(
        UUID(as_uuid=True), ForeignKey("usuarios.id_usuario"), nullable=False
    )
    id_usuario_edita = Column(
        UUID(as_uuid=True), ForeignKey("usuarios.id_usuario"), nullable=True
    )

    # Relaciones //aquí van las relaciones de cada entidad
    Tipo_animal = relationship("Tipo_animal", back_populates="razas", overlaps="Tipo_animal,Raza")  
    animal = relationship("Animal", back_populates="raza", cascade="all, delete-orphan", overlaps="raza,animales")

    # Relaciones de auditoría
    usuario_crea = relationship("usuario", foreign_keys=[id_usuario_crea], overlaps="usuario,usuario_crea,Raza")
    usuario_edita = relationship("usuario", foreign_keys=[id_usuario_edita], overlaps="usuario,usuario_edita,Raza")

    def __repr__(self):
        """Representación en string del objeto Usuario"""
        return f"<id_raza(id={self.id_raza}, nombreRaza='{self.nombreRaza}', id_tipoAnimal='{self.id_tipoAnimal}')>"
    
    def to_dict(self):
        """Convierte el objeto a un diccionario"""
        return {
            'id_raza': self.id_raza,
            'nombreRaza': self.nombreRaza,
            'id_tipoAnimal': self.id_tipoAnimal
        }