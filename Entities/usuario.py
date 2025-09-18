"""
Entidad Usuario
===============

Modelo de Usuario con SQLAlchemy y esquemas de validación con Pydantic.
"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean, UUID, func
from sqlalchemy.orm import relationship
from pydantic import BaseModel, EmailStr, Field, validator
from datetime import datetime
from typing import Optional, List

from Database.config import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id_usuario = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False, index=True)
    telefono = Column(String(20))

    

    
    # Relaciones
    usuarios = relationship("Usuario", back_populates="Animal", cascade="all, delete-orphan") 
    
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