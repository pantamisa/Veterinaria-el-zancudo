"""API de Servicios - Endpoints para gestión de servicios
Veterinaria El Zancudo
"""

import os
import sys
repo_root = os.path.dirname(os.path.dirname(__file__))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)


from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from Database.config import SessionLocal
from Crud.Servicio_crud import (
    crear_servicio,
    obtener_servicios,
    obtener_servicio,
    actualizar_servicio,
    eliminar_servicio,
    obtener_costo_servicio,
    obtener_servicios_con_uso
)

from Schemas import (
    ServicioCreate,
    ServicioUpdate,
    ServicioResponse,
    RespuestaAPI,
    ServicioConUsoResponse
)

router = APIRouter(prefix="/servicios", tags=["Servicios"])


# Dependency para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/estadisticas/uso", response_model=List[ServicioConUsoResponse])
async def obtener_todos_servicios_con_uso(db: Session = Depends(get_db)):

    try:
        servicios = obtener_servicios_con_uso(db)
        return servicios
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener servicios con uso: {str(e)}"
        )



@router.get("/", response_model=List[ServicioResponse])
async def listar_servicios(db: Session = Depends(get_db)):
    """Listar todos los servicios"""
    try:
        servicios = obtener_servicios(db)
        return servicios
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error al listar servicios: {str(e)}")


@router.get("/{id_servicio}", response_model=ServicioResponse)
async def obtener_servicio_por_id(id_servicio: UUID, db: Session = Depends(get_db)):
    """Obtener un servicio por su id"""
    try:
        servicio = obtener_servicio(db, id_servicio)
        if not servicio:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Servicio no encontrado")
        return servicio
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error al obtener servicio: {str(e)}")


@router.post("/", response_model=ServicioResponse, status_code=status.HTTP_201_CREATED)
async def crear_nuevo_servicio(servicio: ServicioCreate, db: Session = Depends(get_db)):
    """Crear un nuevo servicio"""
    try:
        # Verificar existencia por nombre
        existentes = [s for s in obtener_servicios(db) if s.nombre_ser == servicio.nombre_ser]
        if existentes:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El nombre de servicio ya existe")

        nuevo = crear_servicio(db, nombre_ser=servicio.nombre_ser, costo=servicio.costo)
        return nuevo
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error al crear servicio: {str(e)}")


@router.put("/{id_servicio}", response_model=ServicioResponse)
async def actualizar_servicio_endpoint(id_servicio: UUID, datos: ServicioUpdate, db: Session = Depends(get_db)):
    """Actualizar un servicio (parcial)"""
    try:
        campos = {k: v for k, v in datos.dict(exclude_unset=True).items() if v is not None}
        if not campos:
            servicio = obtener_servicio(db, id_servicio)
            if not servicio:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Servicio no encontrado")
            return servicio

        servicio_actualizado = actualizar_servicio(db, id_servicio, **campos)
        if not servicio_actualizado:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Servicio no encontrado")
        return servicio_actualizado
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error al actualizar servicio: {str(e)}")


@router.delete("/{id_servicio}", response_model=RespuestaAPI)
async def eliminar_servicio_endpoint(id_servicio: UUID, db: Session = Depends(get_db)):
    """Eliminar un servicio por id"""
    try:
        eliminado = eliminar_servicio(db, id_servicio)
        if not eliminado:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Servicio no encontrado")
        return RespuestaAPI(mensaje="Servicio eliminado", exito=True, datos={"id_eliminado": str(id_servicio)})
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error al eliminar servicio: {str(e)}")


@router.get("/{id_servicio}/costo", response_model=RespuestaAPI)
async def obtener_costo(id_servicio: UUID, db: Session = Depends(get_db)):
    """Obtener únicamente el costo de un servicio"""
    try:
        costo = obtener_costo_servicio(db, id_servicio)
        if costo is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Servicio no encontrado")
        return RespuestaAPI(mensaje="Costo obtenido", exito=True, datos={"costo": costo})
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error al obtener costo: {str(e)}")


if __name__ == "__main__":
    # Permitir ejecutar este archivo directamente para desarrollo.
    # Ajusta el sys.path a la raíz del proyecto y arranca el servidor uvicorn
    import os
    import sys
    import uvicorn

    repo_root = os.path.dirname(os.path.dirname(__file__))
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)

    # Arrancar la app principal
    uvicorn.run("Main_api:app", host="127.0.0.1", port=8000, reload=True)
