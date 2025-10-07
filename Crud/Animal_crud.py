from sqlalchemy.orm import Session
from Entities.animal import Animal, AnimalCreate, AnimalUpdate  # ajusta el import a tu estructura real
import uuid
from sqlalchemy.orm import Session
from Entities.animal import Animal
import uuid
from datetime import datetime

class AnimalCRUD:

    @staticmethod
    def create(db: Session, animal_in: AnimalCreate) -> Animal:
        """Crear un nuevo animal"""
        db_animal = Animal(**animal_in.dict())
        db.add(db_animal)
        db.commit()
        db.refresh(db_animal)
        return db_animal

    @staticmethod
    def get(db: Session, animal_id: uuid.UUID) -> Animal | None:
        """Obtener un animal por su id"""
        return db.query(Animal).filter(Animal.id_animal == animal_id).first()

    @staticmethod
    def get_by_owner(db: Session, id_usuario: uuid.UUID) -> list[Animal]:
        """Obtener animales por propietario"""
        return db.query(Animal).filter(Animal.id_usuario == id_usuario).all()

    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> list[Animal]:
        """Listar animales con relaciones cargadas"""
        return db.query(Animal).offset(skip).limit(limit).all()

    @staticmethod
    def update(db: Session, animal_id: uuid.UUID, animal_in: AnimalUpdate, id_usuario_edita: uuid.UUID) -> Animal | None:
        """Actualizar un animal"""
        db_animal = db.query(Animal).filter(Animal.id_animal == animal_id).first()
        if not db_animal:
            return None

        update_data = animal_in.dict(exclude_unset=True)
        # Agregar usuario editor y fecha
        update_data['id_usuario_edita'] = id_usuario_edita
        
        for field, value in update_data.items():
            setattr(db_animal, field, value)

        db.commit()
        db.refresh(db_animal)
        return db_animal

    @staticmethod
    def delete(db: Session, animal_id: uuid.UUID) -> bool:
        """Eliminar un animal"""
        db_animal = db.query(Animal).filter(Animal.id_animal == animal_id).first()
        if not db_animal:
            return False

        db.delete(db_animal)
        db.commit()
        return True
