from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship
from datetime import datetime
from Database.config import Base

import uuid  # para generar UUIDs por defecto
from sqlalchemy.dialects.postgresql import UUID  # ESTE es el tipo de SQLAlchemy para columnas UUID

class Raza_animal(Base):
    """
    Modelo de Raza_animal que representa la tabla 'Raza_animal'
    
    Atributos:
        id_raza: Identificador único de cada raza de animal
        nombreRaza: Nombre de la raza del animal (único)
        id_tipoAnimal: tipo de animal al que pertenece la raza (clave foránea)
    """
    
    __tablename__ = 'Raza_animal'
    
    id_raza = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    nombreRaza = Column(String(100), nullable=False)

    # Aquí NO pongas autoincrement en claves foráneas, solo en primarias enteras
    id_tipoAnimal = Column(Integer, ForeignKey('Tipo_animal.id_tipoAnimal'), nullable=False)

    id_usuario_crea = Column(UUID(as_uuid=True), nullable=False)
    id_usuario_edita = Column(UUID(as_uuid=True), nullable=True, default=None)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

    # Relaciones
    tipo_animal = relationship("Tipo_animal", back_populates="razas")
    usuario_crea_rel = relationship("usuario", foreign_keys=[id_usuario_crea])
    usuario_edita_rel = relationship("usuario", foreign_keys=[id_usuario_edita])

    def __repr__(self):
        return f"<Raza_animal(id={self.id_raza}, nombreRaza='{self.nombreRaza}', id_tipoAnimal='{self.id_tipoAnimal}')>"
    
    def to_dict(self):
        return {
            'id_raza': self.id_raza,
            'nombreRaza': self.nombreRaza,
            'id_tipoAnimal': self.id_tipoAnimal
        }
