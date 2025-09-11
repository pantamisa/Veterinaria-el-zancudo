from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel, EmailStr, Field, validator
from datetime import datetime
from typing import Optional, List

from ..Database.database import Base
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


    
    # Relaciones //aquí van las relaciones de cada tabla
    id_tipoAnimal = relationship("Tipo_animal", back_populates="razas")   

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