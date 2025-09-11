from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..Database.database import Base

class Tipo_animal(Base):
    """
    Modelo que representa la tabla 'Tipo_animal'
    
    Atributos:
        id_tipoAnimal: Identificador único del tipo de animal
        nombre: Nombre del tipo de animal
    """
    __tablename__ = 'Tipo_animal'

    id_tipoAnimal = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre = Column(String(100), nullable=False)

    # Relación con Raza_animal
    razas = relationship("Raza_animal", back_populates="tipo_animal", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Tipo_animal(id_tipoAnimal={self.id_tipoAnimal}, nombre='{self.nombre}')>"

    def to_dict(self):
        return {
            'id_tipoAnimal': self.id_tipoAnimal,
            'nombre': self.nombre
        }