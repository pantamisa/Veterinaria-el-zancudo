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

    # PK UUID
    id_usuario = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)

    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False, index=True)
    telefono = Column(String(20))
    contraseña_hash = Column(String(255), nullable=False)
    activo = Column(Boolean, default=True)
    es_admin = Column(Boolean, default=False)

    animales = relationship("Animal", back_populates="usuario", foreign_keys="Animal.id_usuario")
    citas_creadas = relationship("Citas", back_populates="usuario_creador", foreign_keys="Citas.id_usuario_crea")
    citas_editadas = relationship("Citas", back_populates="usuario_editor", foreign_keys="Citas.id_usuario_edita")
    facturas_pagadas = relationship("Factura", back_populates="usuario_pago", foreign_keys="Factura.id_usuario_pago")


    def __repr__(self):
        return f"<Usuario(id_usuario={self.id_usuario}, nombre='{self.nombre}', email='{self.email}')>"

    def to_dict(self):
        return {
            'id_usuario': self.id_usuario,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'telefono': self.telefono,
            'activo': self.activo,
            'es_admin': self.es_admin,
        }