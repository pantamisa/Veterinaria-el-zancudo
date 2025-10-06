"""API de Citas - Endpoints para gestión de citas
Veterinaria El Zancudo
"""

from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from Database.config import SessionLocal
from Crud.Citas_crud import (
    crear_cita,
    obtener_citas,
    obtener_cita,
    obtener_citas_por_animal,
    obtener_citas_pendientes,
    actualizar_cita,
    eliminar_cita
)

from Schemas import (
    CitaCreate,
    CitaResponse,
    CitaUpdate,
    RespuestaAPI
)

router = APIRouter(prefix="/citas", tags=["Citas"])


# Dependency para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[CitaResponse])
async def listar_citas(db: Session = Depends(get_db)):
    """Listar todas las citas"""
    try:
        citas = obtener_citas(db)
        return citas
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error al listar citas: {str(e)}")


@router.get("/{id_cita}", response_model=CitaResponse)
async def obtener_cita_por_id(id_cita: UUID, db: Session = Depends(get_db)):
    """Obtener una cita por su id"""
    try:
        cita = obtener_cita(db, id_cita)
        if not cita:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cita no encontrada")
        return cita
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error al obtener cita: {str(e)}")


@router.post("/", response_model=CitaResponse, status_code=status.HTTP_201_CREATED)
async def crear_nueva_cita(payload: CitaCreate, db: Session = Depends(get_db)):
    """Crear una nueva cita"""
    try:
        nueva = crear_cita(db, id_servicio=payload.id_servicio, id_animal=payload.id_animal, id_usuario_crea=payload.id_usuario_crea, fecha_atencion=payload.fecha_atencion)
        return nueva
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error al crear cita: {str(e)}")


@router.get("/animal/{id_animal}", response_model=List[CitaResponse])
async def citas_por_animal(id_animal: UUID, db: Session = Depends(get_db)):
    """Obtener citas de un animal específico"""
    try:
        citas = obtener_citas_por_animal(db, id_animal)
        return citas
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error al obtener citas por animal: {str(e)}")


@router.get("/pendientes", response_model=List[CitaResponse])
async def citas_pendientes(db: Session = Depends(get_db)):
    """Obtener citas pendientes (sin fecha de atención)"""
    try:
        citas = obtener_citas_pendientes(db)
        return citas
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error al obtener citas pendientes: {str(e)}")


@router.put("/{id_cita}", response_model=CitaResponse)
async def actualizar_cita_endpoint(id_cita: UUID, datos: CitaUpdate, db: Session = Depends(get_db)):
    """Actualizar una cita (parcial)"""
    try:
        campos = {k: v for k, v in datos.dict(exclude_unset=True).items() if v is not None}
        if not campos:
            cita = obtener_cita(db, id_cita)
            if not cita:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cita no encontrada")
            return cita

        cita_actualizada = actualizar_cita(db, id_cita, **campos)
        if not cita_actualizada:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cita no encontrada")
        return cita_actualizada
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error al actualizar cita: {str(e)}")


@router.delete("/{id_cita}", response_model=RespuestaAPI)
async def eliminar_cita_endpoint(id_cita: UUID, db: Session = Depends(get_db)):
    """Eliminar una cita por id"""
    try:
        eliminado = eliminar_cita(db, id_cita)
        if not eliminado:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cita no encontrada")
        return RespuestaAPI(mensaje="Cita eliminada", exito=True, datos={"id_eliminado": str(id_cita)})
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error al eliminar cita: {str(e)}")
