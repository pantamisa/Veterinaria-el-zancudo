from sqlalchemy.orm import Session
from datetime import datetime
from Entities.Factura import Factura  # importa tu modelo Factura
from sqlalchemy import func
from Schemas import FacturaUpdate # Importar el schema para el tipado
# ========== CREAR ==========
def crear_factura(db: Session, id_cita, costo, id_usuario_pago):
    """Crea una nueva factura (por defecto no pagada)."""
    nueva_factura = Factura(
        id_cita=id_cita,
        costo=costo,
        id_usuario_pago=id_usuario_pago,
        pagada=False
    )
    db.add(nueva_factura)
    db.commit()
    db.refresh(nueva_factura)
    return nueva_factura

# ========== LISTAR TODAS ==========
def obtener_facturas(db: Session):
    """Obtiene todas las facturas."""
    return db.query(Factura).all()

# ========== OBTENER POR ID ==========
def obtener_factura(db: Session, id_factura):
    """Obtiene una factura por su id."""
    return db.query(Factura).filter(Factura.id_factura == id_factura).first()

# ========== ACTUALIZAR (MARCAR PAGADA) ==========
def marcar_factura_pagada(db: Session, id_factura):
    """Marca una factura como pagada y guarda fecha de pago."""
    factura = db.query(Factura).filter(Factura.id_factura == id_factura).first()
    if factura:
        factura.pagada = True
        factura.fecha_pago = datetime.utcnow()
        db.commit()
        db.refresh(factura)
    return factura

# ========== ACTUALIZAR FACTURA (GENERAL) ==========
def actualizar_factura(db: Session, id_factura: str, payload: FacturaUpdate):
    """Actualiza una factura existente con los datos proporcionados."""
    factura = db.query(Factura).filter(Factura.id_factura == id_factura).first()
    if factura:
        # Obtener los datos del payload que no son None
        update_data = payload.dict(exclude_unset=True)
        
        # Actualizar los campos de la factura
        for key, value in update_data.items():
            setattr(factura, key, value)
            
        db.commit()
        db.refresh(factura)
    return factura

# ========== ELIMINAR ==========
def eliminar_factura(db: Session, id_factura):
    """Elimina una factura por id."""
    factura = db.query(Factura).filter(Factura.id_factura == id_factura).first()
    if factura:
        db.delete(factura)
        db.commit()
    return factura


def sumar_costos(db: Session) -> float:
    """
    Devuelve la suma total de los costos de todas las facturas.
    """
    total = db.query(func.sum(Factura.costo)).scalar()  # ✅ Suma de todos los costos
    return float(total or 0)  