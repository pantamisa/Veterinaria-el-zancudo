"""
API de Tipos de Animales - Endpoints para gestión de tipos de animales
Veterinaria El Zancudo
"""

from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from Database.config import SessionLocal
from Crud.Tipoanimal_crud import TipoAnimalCRUD
from Entities.Tipo_animal import Tipo_animal
from Schemas import TipoAnimalCreate, TipoAnimalUpdate, TipoAnimalResponse, RespuestaAPI

router = APIRouter(prefix="/tipos-animales", tags=["Tipos de Animales"])


# ==================== DEPENDENCIA DB ====================


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==================== ENDPOINTS GET ====================


@router.get("/", response_model=List[TipoAnimalResponse])
async def obtener_tipos_animales(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    """
    Obtener todos los tipos de animales con paginación.

    - **skip**: Número de registros a saltar (paginación)
    - **limit**: Número máximo de registros a devolver
    """
    try:
        crud = TipoAnimalCRUD(db)
        tipos = crud.obtener_tipos(skip=skip, limit=limit)
        return tipos
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener tipos de animales: {str(e)}",
        )


@router.get("/{id_tipoAnimal}", response_model=TipoAnimalResponse)
async def obtener_tipo_animal_por_id(
    id_tipoAnimal: UUID, db: Session = Depends(get_db)
):
    """
    Obtener un tipo de animal específico por su ID.

    - **id_tipoAnimal**: UUID del tipo de animal a buscar
    """
    try:
        crud = TipoAnimalCRUD(db)
        tipo = crud.obtener_tipo_animal(id_tipoAnimal)
        if not tipo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tipo de animal no encontrado",
            )
        return tipo
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener tipo de animal: {str(e)}",
        )


@router.get("/nombre/{nombre}", response_model=TipoAnimalResponse)
async def obtener_tipo_animal_por_nombre(nombre: str, db: Session = Depends(get_db)):
    """
    Obtener un tipo de animal por su nombre.

    - **nombre**: Nombre del tipo de animal
    """
    try:
        crud = TipoAnimalCRUD(db)
        tipo = crud.obtener_tipo_por_nombre(nombre)
        if not tipo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tipo de animal no encontrado",
            )
        return tipo
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener tipo de animal por nombre: {str(e)}",
        )


# ==================== ENDPOINTS POST ====================


@router.post(
    "/", response_model=TipoAnimalResponse, status_code=status.HTTP_201_CREATED
)
async def crear_tipo_animal(tipo_data: TipoAnimalCreate, db: Session = Depends(get_db)):
    """
    Crear un nuevo tipo de animal en el sistema.

    - **nombre**: Nombre del tipo de animal (único)
    """
    try:
        crud = TipoAnimalCRUD(db)
        # Verificar si ya existe un tipo con el mismo nombre
        existente = crud.obtener_tipo_por_nombre(tipo_data.nombre)
        if existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El tipo de animal ya existe",
            )

        nuevo_tipo = crud.crear_tipo_animal(nombre=tipo_data.nombre)
        return nuevo_tipo
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al crear tipo de animal: {str(e)}",
        )


# ==================== ENDPOINTS PUT ====================


@router.put("/{id_tipoAnimal}", response_model=TipoAnimalResponse)
async def actualizar_tipo_animal(
    id_tipoAnimal: UUID, tipo_data: TipoAnimalUpdate, db: Session = Depends(get_db)
):
    """
    Actualizar la información de un tipo de animal.

    - **id_tipoAnimal**: UUID del tipo de animal a actualizar
    - **nombre**: Nuevo nombre del tipo de animal
    """
    try:
        crud = TipoAnimalCRUD(db)
        tipo_existente = crud.obtener_tipo_animal(id_tipoAnimal)
        if not tipo_existente:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tipo de animal no encontrado",
            )

        # Si se intenta cambiar el nombre, validar que no exista
        if tipo_data.nombre:
            duplicado = crud.obtener_tipo_por_nombre(tipo_data.nombre)
            if duplicado and duplicado.id_tipoAnimal != id_tipoAnimal:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Ya existe un tipo de animal con ese nombre",
                )

        tipo_actualizado = crud.actualizar_tipo_animal(
            id_tipoAnimal, **tipo_data.dict(exclude_unset=True)
        )
        return tipo_actualizado

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al actualizar tipo de animal: {str(e)}",
        )


# ==================== ENDPOINTS DELETE ====================


@router.delete("/{id_tipoAnimal}", response_model=RespuestaAPI)
async def eliminar_tipo_animal(id_tipoAnimal: UUID, db: Session = Depends(get_db)):
    """
    Eliminar un tipo de animal del sistema.

    ⚠️ ADVERTENCIA: Esta acción podría afectar registros que dependan de este tipo.

    - **id_tipoAnimal**: UUID del tipo de animal a eliminar
    """
    try:
        crud = TipoAnimalCRUD(db)
        tipo_existente = crud.obtener_tipo_animal(id_tipoAnimal)
        if not tipo_existente:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tipo de animal no encontrado",
            )

        eliminado = crud.eliminar_tipo_animal(id_tipoAnimal)
        if eliminado:
            return RespuestaAPI(
                mensaje="Tipo de animal eliminado exitosamente",
                exito=True,
                datos={"id_eliminado": str(id_tipoAnimal)},
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error al eliminar tipo de animal",
            )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al eliminar tipo de animal: {str(e)}",
        )
