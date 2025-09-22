import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey, CHAR
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from Database.config import Base

class Animal(Base):
    __tablename__ = 'animales'

    id_animal = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    id_usuario = Column(UUID(as_uuid=True), ForeignKey('usuarios.id_usuario'), nullable=False)
    nombre_animal = Column(String(200), nullable=False, index=True)
    edad_animal = Column(CHAR(4), nullable=False)
    id_genero = Column(UUID(as_uuid=True), ForeignKey('generos.id_genero'), nullable=False)
    id_raza = Column(UUID(as_uuid=True), ForeignKey('Raza_animal.id_raza'), nullable=False)

    # Trazabilidad
    id_usuario_crea = Column(UUID(as_uuid=True), ForeignKey('usuarios.id_usuario'), nullable=False)
    id_usuario_edita = Column(UUID(as_uuid=True), ForeignKey('usuarios.id_usuario'), nullable=True)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

    # 🔹 Relaciones con Usuario (especificando foreign_keys)
    # 🔹 Relaciones con Usuario
    usuario_propietario = relationship(
        "Usuario",
        back_populates="animales",
        foreign_keys=[id_usuario]
    )
    usuario_creador = relationship(
        "Usuario",
        back_populates="animales_creados",
        foreign_keys=[id_usuario_crea]
    )
    usuario_editor = relationship(
        "Usuario",
        back_populates="animales_editados",
        foreign_keys=[id_usuario_edita]
    )

    # 🔹 Relación con otras tablas

    raza = relationship("Raza_animal", back_populates="animales")
    genero = relationship("Genero", back_populates="animales")
    citas = relationship("Citas", back_populates="animal", cascade="all, delete-orphan")




    def __repr__(self):
        return f"<Animal(id_animal={self.id_animal}, nombre_animal='{self.nombre_animal}')>"