import uuid
from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from Database.config import Base

class Usuario(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False, index=True)
    telefono = Column(String(20))
    contraseña_hash = Column(String(255), nullable=False)
    es_admin = Column(Boolean, default=False)

    # 🔹 Relación con animales (propietario)
    animales = relationship(
        "Animal",
        back_populates="usuario_propietario",
        foreign_keys="Animal.id_usuario"
    )

    animales_creados = relationship(
        "Animal",
        back_populates="usuario_creador",
        foreign_keys="Animal.id_usuario_crea"
    )

    animales_editados = relationship(
        "Animal",
        back_populates="usuario_editor",
        foreign_keys="Animal.id_usuario_edita"
    )

    # ✅ CORREGIDO: Sin back_populates porque Factura no lo tiene
    facturas_pagadas = relationship("Factura", foreign_keys="Factura.id_usuario_pago")

    def __repr__(self):
        return f"<Usuario(id_usuario={self.id_usuario}, nombre={self.nombre})>"

