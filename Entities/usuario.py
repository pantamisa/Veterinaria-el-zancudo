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

from ..database.database import Base

class Usuario(Base):
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
    
    id_Usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False, index=True)
    telefono = Column(String(20), nullable=True)
    activo = Column(Boolean, default=True, nullable=False)
    fecha_registro = Column(DateTime, default=datetime.now, nullable=False)
    fecha_actualizacion = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    # Relaciones
    productos = relationship("Producto", back_populates="usuario", cascade="all, delete-orphan")
    
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