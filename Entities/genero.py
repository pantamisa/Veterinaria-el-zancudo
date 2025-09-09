"""
Entidad Animal
===============

Modelo de Usuario con SQLAlchemy y esquemas de validación con Pydantic.
"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from pydantic import BaseModel, EmailStr, Field, validator
from datetime import datetime
from typing import Optional, List

from ..Database.database import Base
from uuid import UUID
class Genero(Base):
    """
    Modelo de Usuario que representa la tabla 'usuarios'
    
    Atributos:
        id: Identificador único del usuario
        nombre: Nombre completo del usuario
        email: Correo electrónico del usuario (único)
        telefono: Número de teléfono del usuario
        activo: Estado del usuario (activo/inactivo)
        fecha_registro: Fecha y hora de registro
        fecha_actualizacion: Fecha y hora de última actualización
    """
    
    __tablename__ = 'Genero'
    
    id_generp = Column(UUID, primary_key=True, autoincrement=True)
    nombre_genero = Column(String(10), nullable=False)
    
    # Relaciones
    animal = relationship("Producto", back_populates="Animal", cascade="all, delete-orphan")

    def __repr__(self):
        """Representación en string del objeto Usuario"""
        return f"<Usuario(id={self.id}, nombre='{self.nombre}', email='{self.email}')>"
    
    def to_dict(self):
        """Convierte el objeto a un diccionario"""
        return {
            'id_genero': self.id_generp,
            'nombre_genero': self.nombre_genero,
        }