from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy import func
from Entities.Raza_animal import Raza_animal
from Entities.animal import Animal
from Entities.Tipo_animal import Tipo_animal
import uuid

class RazaAnimalCRUD:
    def __init__(self, db: Session):
        self.db = db

    def crear_raza_animal(self, nombreRaza: str, id_tipoAnimal: uuid.UUID) -> Raza_animal:
        """Crear una nueva raza de animal"""
        raza = Raza_animal(
            nombreRaza=nombreRaza,
            id_tipoAnimal=id_tipoAnimal,
        )
        self.db.add(raza)
        self.db.commit()
        self.db.refresh(raza)
        return raza

    def obtener_raza(self, id_raza: uuid.UUID) -> Optional[Raza_animal]:
        """Obtener una raza de animal por ID"""
        return self.db.query(Raza_animal).filter(Raza_animal.id_raza == id_raza).first()

    def obtener_raza_por_nombre(self, nombreRaza: str) -> Optional[Raza_animal]:
        """Obtener una raza de animal por nombre"""
        return (
            self.db.query(Raza_animal)
            .filter(Raza_animal.nombreRaza == nombreRaza)
            .first()
        )

    def obtener_razas(self, skip: int = 0, limit: int = 100) -> List[Raza_animal]:
        """Obtener lista de razas con paginación"""
        return self.db.query(Raza_animal).offset(skip).limit(limit).all()

    def obtener_razas_por_tipo(self, id_tipoAnimal: uuid.UUID, skip: int = 0, limit: int = 100) -> List[Raza_animal]:
        """Obtener todas las razas de un tipo de animal"""
        return (
            self.db.query(Raza_animal)
            .filter(Raza_animal.id_tipoAnimal == id_tipoAnimal)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def actualizar_raza_animal(self, id_raza: uuid.UUID, **kwargs) -> Optional[Raza_animal]:
        """Actualizar una raza de animal"""
        raza = self.obtener_raza(id_raza)
        if raza:
            for key, value in kwargs.items():
                if hasattr(raza, key):
                    setattr(raza, key, value)
            self.db.commit()
            self.db.refresh(raza)
        return raza

    def eliminar_raza_animal(self, id_raza: uuid.UUID) -> bool:
        """Eliminar una raza de animal"""
        raza = self.obtener_raza(id_raza)
        if raza:
            self.db.delete(raza)
            self.db.commit()
            return True
        return False

    def obtener_razas_mas_populares(self, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Obtiene las razas más populares (con más animales registrados).
        
        Args:
            limit: Cantidad máxima de resultados (default: 10)
        """
        resultados = self.db.query(
            Raza_animal.id_raza,
            Raza_animal.nombreRaza,
            Tipo_animal.nombre.label('tipo_animal'),
            func.count(Animal.id_animal).label('total_animales')
        ).join(
            Animal, Raza_animal.id_raza == Animal.id_raza
        ).join(
            Tipo_animal, Raza_animal.id_tipoAnimal == Tipo_animal.id_tipoAnimal
        ).group_by(
            Raza_animal.id_raza,
            Raza_animal.nombreRaza,
            Tipo_animal.nombre
        ).order_by(
            func.count(Animal.id_animal).desc()
        ).limit(limit).all()

        razas_populares = [
            {
                "id_raza": str(row.id_raza),
                "nombre_raza": row.nombreRaza,
                "tipo_animal": row.tipo_animal,
                "total_animales": row.total_animales
            }
            for row in resultados
        ]

        return razas_populares