from sqlalchemy.orm import Session
from Entities.usuario import Usuario
from .utils_password import hash_password, verify_password
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
# Eliminar usuario
def delete_usuario(db: Session, id_usuario: uuid.UUID) -> bool:
    """
    Elimina un usuario manejando todas las relaciones Foreign Key
    """
    try:
        usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        if not usuario:
            return False

        # 1. Manejar facturas - NO se pueden poner NULL porque es NOT NULL
        # Opción A: Eliminar las facturas asociadas
        from Entities.Factura import Factura
        facturas = db.query(Factura).filter(Factura.id_usuario_pago == id_usuario).all()
        for factura in facturas:
            db.delete(factura)
        
        # 2. Manejar animales donde este usuario es propietario
        from Entities.animal import Animal
        animales_propietario = db.query(Animal).filter(Animal.id_usuario == id_usuario).all()
        for animal in animales_propietario:
            # Opción: Eliminar los animales (y sus citas por cascade)
            db.delete(animal)
        
        # 3. Manejar animales creados por este usuario
        animales_creados = db.query(Animal).filter(Animal.id_usuario_crea == id_usuario).all()
        for animal in animales_creados:
            # Poner NULL o asignar a otro usuario
            animal.id_usuario_crea = None
        
        # 4. Manejar animales editados por este usuario
        animales_editados = db.query(Animal).filter(Animal.id_usuario_edita == id_usuario).all()
        for animal in animales_editados:
            animal.id_usuario_edita = None
        
        # 5. Manejar citas creadas por este usuario
        from Entities.Citas import Citas
        citas_creadas = db.query(Citas).filter(Citas.id_usuario_crea == id_usuario).all()
        for cita in citas_creadas:
            cita.id_usuario_crea = None
        
        # 6. Manejar citas editadas por este usuario
        citas_editadas = db.query(Citas).filter(Citas.id_usuario_edita == id_usuario).all()
        for cita in citas_editadas:
            cita.id_usuario_edita = None

        # Ahora sí eliminar el usuario
        db.delete(usuario)
        db.commit()
        return True
        
    except Exception as e:
        db.rollback()
        print(f"Error al eliminar usuario: {e}")
        return False
    
# Login (comprueba email + password)
def login_usuario(db: Session, email: str, password: str) -> Usuario | None:
    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not usuario:
        return None
    if not verify_password(password, usuario.contraseña_hash):
        return None
    return usuario

def contar_usuarios(db: Session) -> int:
    """
    Devuelve la cantidad total de usuarios registrados en la base de datos.
    """
    from Entities.usuario import Usuario
    total = db.query(Usuario).count()
    return total