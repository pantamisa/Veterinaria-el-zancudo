import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from Database.config import Base


class Raza_animal(Base):
    """Modelo de la tabla de razas de animales"""
    __tablename__ = 'Raza_animal'

    id_raza = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    nombreRaza = Column(String(100), nullable=False)
    id_tipoAnimal = Column( UUID, ForeignKey('Tipo_animal.id_tipoAnimal'), nullable=False )

    # 🔹 relaciones ORM
    tipo_animal = relationship("Tipo_animal", back_populates="razas")
    animales = relationship("Animal", back_populates="raza")  # inversa: los animales de esta raza

    def __repr__(self):
        return (
            f"<Raza_animal(id={self.id_raza}, "
            f"nombreRaza='{self.nombreRaza}', id_tipoAnimal='{self.id_tipoAnimal}')>"
        )

    def to_dict(self):
        return {
            'id_raza': self.id_raza,
            'nombreRaza': self.nombreRaza,
            'id_tipoAnimal': self.id_tipoAnimal
        }
