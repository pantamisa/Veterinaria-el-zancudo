"""
Entidad citas
===============

Modelo de Usuario con SQLAlchemy y esquemas de validación con Pydantic.
"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from pydantic import BaseModel, EmailStr, Field, validator
from datetime import datetime
from typing import Optional, List
from uuid import UUID
from ..Database.config import Base

class Citas(Base):
    """
    Modelo de Usuario que representa la tabla 'usuarios'
    
    Atributos:
        id_citas: Identificador único del usuario
        id_Servicio: clave foranea
        id_animal: clave forenea
    """
    
    __tablename__ = 'Citas'
    
    id_Citas = Column(Integer, primary_key=True, autoincrement=True)
  
    fecha_creacion = Column(DateTime, default=datetime.now, nullable=False)
    fecha_atencion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    fecha_edicion = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    # Relaciones
    productos = relationship("Producto", back_populates="usuario", cascade="all, delete-orphan")
    Servicios  = relationship("Servicio", back_populates="productos", cascade="all, delete-orphan")
    Animal = relationship("Animal", back_populates="productos", cascade="all, delete-orphan")
    



    def __repr__(self):
        """Representación en string del objeto Usuario"""
        return f"<Citas(id={self.id_Citas}')>"
    
    def to_dict(self):
        """Convierte el objeto a un diccionario"""
        return {
            'id': self.id_Citas,
            'fecha_creacion': self.fecha_creacion.isoformat() if self.fecha_creacion else None,
            'fecha_atencion': self.fecha_atencion.isoformat() if self.fecha_atencion else None,
            'fecha_edicion': self.fecha_edicion.isoformat() if self.fecha_edicion else None
        }