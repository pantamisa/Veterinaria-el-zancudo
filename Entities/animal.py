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
from uuid import UUID

from ..Database.database import Base

class Animal(Base):
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
    
    __tablename__ = 'Animal'
    
    id_animal = Column(UUID, primary_key=True, autoincrement=True)
    nombre_animal = Column(String(100), nullable=False)
    Edad = Column(String(5), nullable=True)

    id_usuario_crar=Column(UUID, ForeignKey('id_Usuario'), nullable=False)
    id_usuario_Editar=Column(UUID, ForeignKey('id_Usuario'), nullable=False)
    fecha_registro = Column(DateTime, default=datetime.now, nullable=False)
    fecha_actualizacion = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    # Relaciones
    usuarios = relationship("Usuario", back_populates="Animal", cascade="all, delete-orphan")
    generos =relationship("Genero", back_populates="Animal", cascade="all, delete-orphan")


    def __repr__(self):
        """Representación en string del objeto Usuario"""
        return f"<Usuario(id={self.id}, nombre='{self.nombre}', email='{self.email}')>"
    
    def to_dict(self):
        """Convierte el objeto a un diccionario"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'telefono': self.telefono,
            'activo': self.activo,
            'fecha_registro': self.fecha_registro.isoformat() if self.fecha_registro else None,
            'fecha_actualizacion': self.fecha_actualizacion.isoformat() if self.fecha_actualizacion else None
        }