
from Database.config import SessionLocal
from Entities.genero import Genero
from Crud.Usuario_crud import create_usuario, login_usuario

def CrearUsuarioPrueba():
    """Crear usuario de prueba con manejo de sesión"""
    db = SessionLocal()
    try:
        # Crear usuario
        nuevo = create_usuario(
            db,
            nombre="Kelvin",
            apellido="Rengifo",
            email="kelvin@example.com",
            telefono="123456",
            password="miClaveSegura"
        )

        print("Usuario creado:", nuevo.to_dict())

        # Login
        usuario_login = login_usuario(db, "kelvin@example.com", "miClaveSegura")
        if usuario_login:
            print("✅ Login correcto:", usuario_login.nombre)
        else:
            print("❌ Credenciales incorrectas")

    except Exception as e:
        print(f"❌ Error al crear usuario: {e}")
        db.rollback()
    finally:
        db.close()

def CrearGeneros():
    """Crear géneros con manejo de sesión"""
    db = SessionLocal()
    try:
        # Verificar si ya existen géneros
        generos_existentes = db.query(Genero).count()
        if generos_existentes > 0:
            print("✅ Los géneros ya existen en la base de datos")
            return

        # Crear géneros
        macho = Genero(nombre_genero="Macho")
        hembra = Genero(nombre_genero="Hembra")
        desconocido = Genero(nombre_genero="Otro")

        # Agregar a la sesión
        db.add_all([macho, hembra, desconocido])
        db.commit()

        # Refrescar para ver los UUID generados
        db.refresh(macho)
        db.refresh(hembra)
        db.refresh(desconocido)

        print("✅ Géneros insertados correctamente")
        print(f"Macho ID: {macho.id_genero}")
        print(f"Hembra ID: {hembra.id_genero}")
        print(f"Otro ID: {desconocido.id_genero}")

    except Exception as e:
        db.rollback()
        print("❌ Error al poblar tabla Género:", e)
    finally:
        db.close()

def poblar_datos_iniciales():
    """Función principal para poblar datos iniciales"""
    print("🔄 Iniciando población de datos...")
    
    # Crear géneros primero
    CrearGeneros()
    
    # Crear usuario de prueba
    CrearUsuarioPrueba()
    
    print("✅ Población de datos completada")

if __name__ == "__main__":
    poblar_datos_iniciales()