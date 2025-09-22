import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from Database.config import Base


class Tipo_animal(Base):
    __tablename__ = 'Tipo_animal'

    # 🔹 Usamos UUID como clave primaria. No pongas autoincrement con UUID.
    id_tipoAnimal = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,  nullable=False )
    nombre = Column(String(100), nullable=False)

    razas = relationship("Raza_animal",back_populates="tipo_animal",cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Tipo_animal(id_tipoAnimal={self.id_tipoAnimal}, nombre='{self.nombre}')>"

    def to_dict(self):
        return {
            'id_tipoAnimal': self.id_tipoAnimal,
            'nombre': self.nombre
        }
