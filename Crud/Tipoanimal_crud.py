from typing import List, Optional
from sqlalchemy.orm import Session
from Entities.Tipo_animal import Tipo_animal
import uuid

class TipoAnimalCRUD:
    def __init__(self, db: Session):
        self.db = db

    def crear_tipo_animal(self, nombre: str) -> Tipo_animal:
        """Crear un nuevo tipo de animal"""
        tipo = Tipo_animal(nombre=nombre)
        self.db.add(tipo)
        self.db.commit()
        self.db.refresh(tipo)
        return tipo

    def obtener_tipo_animal(self, id_tipoAnimal: uuid.UUID) -> Optional[Tipo_animal]:
        """Obtener un tipo de animal por ID"""
        return (
            self.db.query(Tipo_animal)
            .filter(Tipo_animal.id_tipoAnimal == id_tipoAnimal)
            .first()
        )

    def obtener_tipo_por_nombre(self, nombre: str) -> Optional[Tipo_animal]:
        """Obtener tipo de animal por nombre"""
        return self.db.query(Tipo_animal).filter(Tipo_animal.nombre == nombre).first()

    def obtener_tipos(self, skip: int = 0, limit: int = 100) -> List[Tipo_animal]:
        """Obtener lista de tipos de animales con paginación"""
        return self.db.query(Tipo_animal).offset(skip).limit(limit).all()

    def actualizar_tipo_animal(self, id_tipoAnimal: uuid.UUID, **kwargs) -> Optional[Tipo_animal]:
        """Actualizar un tipo de animal"""
        tipo = self.obtener_tipo_animal(id_tipoAnimal)
        if tipo:
            for key, value in kwargs.items():
                if hasattr(tipo, key):
                    setattr(tipo, key, value)
            self.db.commit()
            self.db.refresh(tipo)
        return tipo

    def eliminar_tipo_animal(self, id_tipoAnimal: uuid.UUID) -> bool:
        """Eliminar un tipo de animal"""
        tipo = self.obtener_tipo_animal(id_tipoAnimal)
        if tipo:
            self.db.delete(tipo)
            self.db.commit()
            return True
        return False