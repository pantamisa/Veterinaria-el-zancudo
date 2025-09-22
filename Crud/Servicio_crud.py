from sqlalchemy.orm import Session
from Models.servicios import Servicios  # Ajusta la ruta al modelo correcto

# ========== CREAR ==========
def crear_servicio(db: Session, nombre_ser: str, costo: float):
    """Crea un nuevo servicio."""
    nuevo_servicio = Servicios(
        nombre_ser=nombre_ser,
        costo=costo
    )
    db.add(nuevo_servicio)
    db.commit()
    db.refresh(nuevo_servicio)
    return nuevo_servicio

# ========== LISTAR TODOS ==========
def obtener_servicios(db: Session):
    """Obtiene todos los servicios."""
    return db.query(Servicios).all()

# ========== OBTENER POR ID ==========
def obtener_servicio(db: Session, id_servicio):
    """Obtiene un servicio por su id."""
    return db.query(Servicios).filter(Servicios.id_servicio == id_servicio).first()

# ========== ACTUALIZAR ==========
def actualizar_servicio(db: Session, id_servicio, nombre_ser=None, costo=None):
    """Actualiza campos de un servicio existente."""
    servicio = db.query(Servicios).filter(Servicios.id_servicio == id_servicio).first()
    if not servicio:
        return None
    if nombre_ser:
        servicio.nombre_ser = nombre_ser
    if costo is not None:
        servicio.costo = costo
    db.commit()
    db.refresh(servicio)
    return servicio

# ========== ELIMINAR ==========
def eliminar_servicio(db: Session, id_servicio):
    """Elimina un servicio por id."""
    servicio = db.query(Servicios).filter(Servicios.id_servicio == id_servicio).first()
    if servicio:
        db.delete(servicio)
        db.commit()
    return servicio

# ========== OBTENER SOLO COSTO ==========
def obtener_costo_servicio(db: Session, id_servicio):
    """Devuelve solo el costo del servicio por id."""
    servicio = db.query(Servicios.costo).filter(Servicios.id_servicio == id_servicio).first()
    return servicio[0] if servicio else None
