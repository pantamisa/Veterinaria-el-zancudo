from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship
from pydantic import BaseModel, EmailStr, Field, validator
from datetime import datetime
from typing import Optional, List

from ..Database.config import Base
from uuid import UUID  #ponerselo a los id

class Raza_animal(Base):
    """
    Modelo de Raza_animal que representa la tabla 'Raza_animal'
    
    Atributos:
        id_raza: Identificador único de cada raza de animal
        nombreRaza: Nombre de la raza del animal (único)
        id_tipoAnimal: tipo de animal al que pertenece la raza (clave foranea)
    """
    
    __tablename__ = 'Raza_animal'
    
    id_raza = Column(UUID, Integer, primary_key=True, autoincrement=True, nullable=False) #elegir uno de los dos UUID o Integer
    nombreRaza = Column(String(100), nullable=False)
    id_tipoAnimal=Column(Integer, ForeignKey('Tipo_animal.id_tipoAnimal'), nullable=False, autoincrement=True)
    id_usuario_crea = Column(UUID(as_uuid=True), nullable=False)
    id_usuario_edita = Column(UUID(as_uuid=True), nullable=True, default=None)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

    
    # Relaciones //aquí van las relaciones de cada tabla
    id_tipoAnimal = relationship("Tipo_animal", back_populates="razas")   
    usuario_crea = relationship("usuario", foreign_keys=[id_usuario_crea])
    usuario_edita = relationship("usuario", foreign_keys=[id_usuario_edita])

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