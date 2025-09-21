import uuid
from datetime import datetime

from Database.config import SessionLocal  # tu config
from models.usuario import Usuario
from models.genero import Genero
from models.raza_animal import RazaAnimal   # o el nombre de tu modelo de razas
from models.animal import Animal
from models.cita import Cita               # tu modelo de Citas

def poblar_db():
    db = SessionLocal()
    try:
        # === 1. Usuario ===
        usuario_id = uuid.uuid4()
        usuario = Usuario(
            id_usuario=usuario_id,         # asegúrate que tu PK sea así
            nombre="Admin",
            apellido="Admin",
            email="juan@example.com",
            telefono="3001234567",
            id_usuario_crea=usuario_id
        )
        db.add(usuario)
        db.commit()
        db.refresh(usuario)

        print("Datos insertados correctamente:")
        print(f"Usuario: {usuario.id_usuario}")


    except Exception as e:
        db.rollback()
        print("Error al poblar DB:", e)
    finally:
        db.close()

if __name__ == "__main__":
    poblar_db()