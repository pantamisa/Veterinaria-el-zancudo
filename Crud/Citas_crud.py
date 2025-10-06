from sqlalchemy.orm import Session
from datetime import datetime
from Entities.Citas import Citas  # Ajusta la ruta al modelo correcto

# ========== CREAR ==========
def crear_cita(db: Session, id_servicio, id_animal, id_usuario_crea, fecha_atencion=None):
    """Crea una nueva cita."""
    nueva_cita = Citas(
        id_servicio=id_servicio,
        id_animal=id_animal,
        id_usuario_crea=id_usuario_crea,
        fecha_atencion=fecha_atencion
    )
    db.add(nueva_cita)
    db.commit()
    db.refresh(nueva_cita)
    return nueva_cita

# ========== LISTAR TODAS ==========
def obtener_citas(db: Session):
    """Obtiene todas las citas."""
    return db.query(Citas).all()

# ========== OBTENER POR ID ==========
def obtener_cita(db: Session, id_cita):
    """Obtiene una cita por su id."""
    return db.query(Citas).filter(Citas.id_citas == id_cita).first()

# ========== ACTUALIZAR ==========
def actualizar_cita(db: Session, id_cita, id_servicio=None, id_animal=None, fecha_atencion=None, id_usuario_edita=None):
    """Actualiza campos de una cita existente."""
    cita = db.query(Citas).filter(Citas.id_citas == id_cita).first()
    if not cita:
        return None
    if id_servicio:
        cita.id_servicio = id_servicio
    if id_animal:
        cita.id_animal = id_animal
    if fecha_atencion:
        cita.fecha_atencion = fecha_atencion
    if id_usuario_edita:
        cita.id_usuario_edita = id_usuario_edita
    db.commit()
    db.refresh(cita)
    return cita

# ========== ELIMINAR ==========
def eliminar_cita(db: Session, id_cita):
    """Elimina una cita por id."""
    cita = db.query(Citas).filter(Citas.id_citas == id_cita).first()
    if cita:
        db.delete(cita)
        db.commit()
    return cita
