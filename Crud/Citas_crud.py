from sqlalchemy.orm import Session
from datetime import datetime
from Entities.Citas import Citas  # Ajusta la ruta al modelo correcto
import uuid

def crear_cita(db: Session, id_servicio: uuid.UUID, id_animal: uuid.UUID, id_usuario_crea: uuid.UUID, fecha_atencion=None):
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

def obtener_citas_con_detalles(db: Session):
    """Obtiene todas las citas con información de servicios y animales."""
    return db.query(Citas).options(
        db.joinedload(Citas.servicio),
        db.joinedload(Citas.animal)
    ).all()

def obtener_citas_por_animal(db: Session, id_animal: uuid.UUID):
    """Obtiene las citas de un animal específico."""
    return db.query(Citas).filter(Citas.id_animal == id_animal).all()

def obtener_citas_pendientes(db: Session):
    """Obtiene citas que no han sido atendidas."""
    return db.query(Citas).filter(Citas.fecha_atencion.is_(None)).all()


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
