"""
Entidad Usuario
===============

Modelo de Usuario con SQLAlchemy y esquemas de validación con Pydantic.
"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from pydantic import BaseModel, EmailStr, Field, validator
from datetime import datetime
from typing import Optional, List

from ..Database.database import Base
from uuid import UUID  #ponerselo a los id

class Raza_animal(Base):
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
    
    __tablename__ = 'usuarios'
    
    id_raza = Column(UUID, Integer, primary_key=True, autoincrement=True)
    nombreRaza = Column(String(100), nullable=False)
    Tipoanimal=3


    
    # Relaciones //aquí van las relaciones de cada tabla
    productos = relationship("Producto", back_populates="usuario", cascade="all, delete-orphan")
    
    def __repr__(self):
        """Representación en string del objeto Usuario"""
        return f"<Raza(id={self.id}, nombreRaza='{self.nombre}', email='{self.email}')>"
    
    def to_dict(self):
        """Convierte el objeto a un diccionario"""
        return {
            'id_raza': self.id_raza,
            'nombreRaza': self.nombre,
        }