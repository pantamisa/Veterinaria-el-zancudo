"""API de Facturas - Endpoints para gestión de facturas
Veterinaria El Zancudo
"""

from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from Database.config import SessionLocal
from Crud.Factura_crud import (
    crear_factura,
    obtener_facturas,
    obtener_factura,
    marcar_factura_pagada,
    actualizar_costo_factura,
    eliminar_factura
)

from Schemas import (
    FacturaCreate,
    FacturaResponse,
    FacturaUpdate,
    RespuestaAPI
)

router = APIRouter(prefix="/facturas", tags=["Facturas"])


# Dependency para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[FacturaResponse])
async def listar_facturas(db: Session = Depends(get_db)):
    """Listar todas las facturas"""
    try:
        facturas = obtener_facturas(db)
        return facturas
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error al listar facturas: {str(e)}")


@router.get("/{id_factura}", response_model=FacturaResponse)
async def obtener_factura_por_id(id_factura: UUID, db: Session = Depends(get_db)):
    """Obtener una factura por su id"""
    try:
        factura = obtener_factura(db, id_factura)
        if not factura:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Factura no encontrada")
        return factura
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error al obtener factura: {str(e)}")


@router.post("/", response_model=FacturaResponse, status_code=status.HTTP_201_CREATED)
async def crear_nueva_factura(payload: FacturaCreate, db: Session = Depends(get_db)):
    """Crear una nueva factura"""
    try:
        nueva = crear_factura(db, id_cita=payload.id_cita, costo=payload.costo, id_usuario_pago=payload.id_usuario_pago)
        return nueva
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error al crear factura: {str(e)}")


@router.post("/{id_factura}/pagar", response_model=FacturaResponse)
async def pagar_factura(id_factura: UUID, db: Session = Depends(get_db)):
    """Marcar una factura como pagada"""
    try:
        factura = marcar_factura_pagada(db, id_factura)
        if not factura:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Factura no encontrada")
        return factura
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error al marcar factura como pagada: {str(e)}")


@router.patch("/{id_factura}/costo", response_model=FacturaResponse)
async def actualizar_costo(id_factura: UUID, nuevo_costo: float, db: Session = Depends(get_db)):
    """Actualizar el costo de una factura"""
    try:
        factura = actualizar_costo_factura(db, id_factura, nuevo_costo)
        if not factura:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Factura no encontrada")
        return factura
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error al actualizar costo de factura: {str(e)}")


@router.delete("/{id_factura}", response_model=RespuestaAPI)
async def eliminar_factura_endpoint(id_factura: UUID, db: Session = Depends(get_db)):
    """Eliminar una factura por id"""
    try:
        eliminado = eliminar_factura(db, id_factura)
        if not eliminado:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Factura no encontrada")
        return RespuestaAPI(mensaje="Factura eliminada", exito=True, datos={"id_eliminado": str(id_factura)})
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error al eliminar factura: {str(e)}")
