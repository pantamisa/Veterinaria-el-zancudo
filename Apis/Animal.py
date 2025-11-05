"""
API de Animales - Endpoints para gestión de animales
Veterinaria El Zancudo
"""

from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from Database.config import SessionLocal
from Entities.animal import Animal
from Schemas import (
    AnimalCreate,
    AnimalUpdate,
    AnimalResponse,
    RespuestaAPI,
    AnimalUpdateResponse,
)
from Crud.Animal_crud import AnimalCRUD

router = APIRouter(prefix="/animales", tags=["Animales"])


# ==================== DEPENDENCIA DB ====================


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==================== ENDPOINTS GET ====================


@router.get("/", response_model=List[AnimalResponse])
async def obtener_animales(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    """
    Obtener todos los animales con paginación.

    - **skip**: Número de registros a omitir.
    - **limit**: Número máximo de animales a retornar.
    """
    try:
        animales = AnimalCRUD.get_all(db, skip, limit)
        return animales
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener animales: {str(e)}",
        )


@router.get("/{animal_id}", response_model=AnimalResponse)
async def obtener_animal_por_id(animal_id: UUID, db: Session = Depends(get_db)):
    """
    Obtener un animal por su ID.

    - **animal_id**: UUID del animal.
    """
    try:
        animal = AnimalCRUD.get(db, animal_id)
        if not animal:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Animal no encontrado"
            )
        return animal
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener animal: {str(e)}",
        )


@router.get("/propietario/{id_usuario}", response_model=List[AnimalResponse])
async def obtener_animales_por_propietario(
    id_usuario: UUID, db: Session = Depends(get_db)
):
    """
    Obtener todos los animales registrados por un propietario.

    - **id_usuario**: UUID del usuario propietario.
    """
    try:
        animales = AnimalCRUD.get_by_owner(db, id_usuario)
        return animales
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener animales por propietario: {str(e)}",
        )


# ==================== ENDPOINTS POST ====================


@router.post("/", response_model=AnimalResponse, status_code=status.HTTP_201_CREATED)
async def crear_animal(animal_in: AnimalCreate, db: Session = Depends(get_db)):
    """
    Registrar un nuevo animal en el sistema.

    - **nombre_animal**: Nombre del animal.
    - **especie**: Tipo de especie (perro, gato, etc.).
    - **edad_animal**: Edad en años o meses.
    - **raza**: Raza del animal (opcional).
    - **id_usuario**: Propietario del animal.
    """
    try:
        nuevo_animal = AnimalCRUD.create(db, animal_in)
        return nuevo_animal
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al crear animal: {str(e)}",
        )


# ==================== ENDPOINTS PUT ====================


@router.put("/{animal_id}", response_model=AnimalUpdateResponse)
async def actualizar_animal(
    animal_id: UUID,
    animal_in: AnimalUpdate,
    id_usuario_edita: UUID,
    db: Session = Depends(get_db),
):
    """
    Actualizar información de un animal existente.

    - **animal_id**: UUID del animal.
    - **animal_in**: Campos a actualizar.
    - **id_usuario_edita**: Usuario que realiza la edición.
    """
    try:
        animal_actualizado = AnimalCRUD.update(
            db, animal_id, animal_in, id_usuario_edita
        )
        if not animal_actualizado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Animal no encontrado"
            )
        return {"exito": True, "data": animal_actualizado}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al actualizar animal: {str(e)}",
        )


# ==================== ENDPOINTS DELETE ====================


@router.delete("/{animal_id}", response_model=RespuestaAPI)
async def eliminar_animal(animal_id: UUID, db: Session = Depends(get_db)):
    """
    Eliminar un animal del sistema.

    - **animal_id**: UUID del animal a eliminar.
    """
    try:
        eliminado = AnimalCRUD.delete(db, animal_id)
        if not eliminado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Animal no encontrado"
            )

        return RespuestaAPI(
            mensaje="Animal eliminado correctamente",
            exito=True,
            datos={"id_eliminado": str(animal_id)},
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al eliminar animal: {str(e)}",
        )


# ==================== ENDPOINT EXTRA ====================


@router.get("/{animal_id}/propietario", response_model=RespuestaAPI)
async def obtener_propietario_animal(animal_id: UUID, db: Session = Depends(get_db)):
    """
    Obtener la información del propietario de un animal.

    - **animal_id**: UUID del animal.
    """
    try:
        animal = AnimalCRUD.get(db, animal_id)
        if not animal:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Animal no encontrado"
            )

        propietario = animal.usuario  # relación esperada en la entidad Animal
        if not propietario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Propietario no encontrado",
            )

        return RespuestaAPI(
            mensaje=f"Propietario encontrado: {propietario.nombre} {propietario.apellido}",
            exito=True,
            datos={
                "id_usuario": str(propietario.id_usuario),
                "nombre": propietario.nombre,
                "apellido": propietario.apellido,
                "email": propietario.email,
            },
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener propietario: {str(e)}",
        )
