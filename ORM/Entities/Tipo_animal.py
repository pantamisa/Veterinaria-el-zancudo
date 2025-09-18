from sqlalchemy import Column, Integer, String, UUID, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel, EmailStr, Field, validator
from ..database.config import Base
import datetime

class Tipo_animal(Base):
    """
    Modelo que representa la tabla 'Tipo_animal'
    
    Atributos:
        id_tipoAnimal: Identificador único del tipo de animal (ave, perro, gato))
        nombre: Nombre del tipo de animal
    """
    __tablename__ = 'Tipo_animal'

    id_tipoAnimal = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    id_usuario_crea = Column(UUID(as_uuid=True), nullable=False)
    id_usuario_edita = Column(UUID(as_uuid=True), nullable=True, default=None)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())


    # Relación con Raza_animal
    razas = relationship("Raza_animal", back_populates="Tipo_animal", cascade="all, delete-orphan")
    
    # Campos de auditoría
    id_usuario_crea = Column(
        UUID(as_uuid=True), ForeignKey("usuarios.id_usuario"), nullable=False
    )
    id_usuario_edita = Column(
        UUID(as_uuid=True), ForeignKey("usuarios.id_usuario"), nullable=True
    )

    # Relaciones de auditoría
    usuario_crea = relationship("usuario", foreign_keys=[id_usuario_crea], overlaps="usuario,usuario_crea,Tipo_animal")
    usuario_edita = relationship("usuario", foreign_keys=[id_usuario_edita], overlaps="usuario,usuario_edita,Tipo_animal")

    def __repr__(self):
        return f"<Tipo_animal(id_tipoAnimal={self.id_tipoAnimal}, nombre='{self.nombre}')>"

    def to_dict(self):
        return {
            'id_tipoAnimal': self.id_tipoAnimal,
            'nombre': self.nombre
        }