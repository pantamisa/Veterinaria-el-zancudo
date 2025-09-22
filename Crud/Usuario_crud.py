from sqlalchemy.orm import Session
from Entities.usuario import Usuario
from utils_password import hash_password, verify_password
import uuid

# Crear usuario (con hash automático)
def create_usuario(db: Session, nombre: str, apellido: str, email: str, telefono: str, password: str, es_admin: bool=False) -> Usuario:
    # hash automático de la contraseña
    hashed = hash_password(password)
    usuario = Usuario(
        id_usuario = uuid.uuid4(),
        nombre = nombre,
        apellido = apellido,
        email = email,
        telefono = telefono,
        contraseña_hash = hashed,
        es_admin = es_admin
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

# Obtener usuario por id
def get_usuario(db: Session, id_usuario: uuid.UUID) -> Usuario | None:
    return db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()

# Actualizar usuario
def update_usuario(db: Session, id_usuario: uuid.UUID, **kwargs) -> Usuario | None:
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    if not usuario:
        return None
    for key, value in kwargs.items():
        if key == 'password':  # si mandan password nueva, hashear
            usuario.contraseña_hash = hash_password(value)
        elif hasattr(usuario, key):
            setattr(usuario, key, value)
    db.commit()
    db.refresh(usuario)
    return usuario

# Eliminar usuario
def delete_usuario(db: Session, id_usuario: uuid.UUID) -> bool:
    usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    if not usuario:
        return False
    db.delete(usuario)
    db.commit()
    return True

# Login (comprueba email + password)
def login_usuario(db: Session, email: str, password: str) -> Usuario | None:
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not usuario:
        return None
    if not verify_password(password, usuario.contraseña_hash):
        return None
    return usuario