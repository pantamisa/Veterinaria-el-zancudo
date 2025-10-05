
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Crud.Usuario_crud import create_usuario, get_usuario, update_usuario, delete_usuario, login_usuario
from Entities.usuario import Usuario
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuración de conexión a Neon (PostgreSQL)
DATABASE_URL = 'postgresql://neondb_owner:npg_MDXR0Zj6mzvY@ep-young-boat-ae7ls9d8-pooler.c-2.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


import uuid

class UsuarioMenu:
    def __init__(self):
        self.db = SessionLocal()

    def pedir_uuid(self, mensaje):
        while True:
            valor = input(mensaje)
            try:
                return str(uuid.UUID(valor))
            except ValueError:
                print("⚠ El valor ingresado no es un UUID válido. Intente de nuevo.")

    def menu(self):
        while True:
            print("\n===== SUBMENÚ USUARIOS =====")
            print("1. Crear Usuario")
            print("2. Consultar Usuario por ID")
            print("3. Actualizar Usuario")
            print("5. Login de Usuario")
            print("6. Listar Usuarios")
            print("7. Eliminar Usuarios")
            print("0. Volver al Menú Principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear_usuario()
            elif opcion == "2":
                self.consultar_usuario()
            elif opcion == "3":
                self.actualizar_usuario()
            elif opcion == "5":
                self.login_usuario()
            elif opcion == "6":
                self.listar_usuarios()
            elif opcion == "7":
                self.borrar_usuario()
            elif opcion == "0":
                print("Volviendo al menú principal...")
                break
            else:
                print("Opción no válida.")

    def crear_usuario(self):
        try:
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            email = input("Email: ")
            telefono = input("Teléfono: ")
            password = input("Contraseña: ")
            usuario = create_usuario(self.db, nombre, apellido, email, telefono, password)
            print("✅ Usuario creado:", usuario)
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            self.db.rollback()

    def consultar_usuario(self):
        id_usuario = self.pedir_uuid("ID del usuario (UUID): ")
        usuario = get_usuario(self.db, id_usuario)
        print("✅ Usuario:", usuario if usuario else "❌ No encontrado")

    def actualizar_usuario(self):
        id_usuario = self.pedir_uuid("ID del usuario a actualizar (UUID): ")
        campo = input("Campo a actualizar (nombre, apellido, email, telefono, password): ")
        valor = input("Nuevo valor: ")
        usuario = update_usuario(self.db, id_usuario, **{campo: valor})
        print("✅ Usuario actualizado:", usuario if usuario else "❌ No encontrado")

    def borrar_usuario(self):
        id_usuario = self.pedir_uuid("ID del usuario a actualizar (UUID): ")
        usuario = delete_usuario(self.db, id_usuario)
        print("✅ Usuario Eliminado:", usuario if usuario else "❌ No encontrado")


    def login_usuario(self):
        email = input("Email: ")
        password = input("Contraseña: ")
        usuario = login_usuario(self.db, email, password)
        print("✅ Login exitoso:", usuario if usuario else "❌ Credenciales inválidas")

    def listar_usuarios(self):
        usuarios = self.db.query(Usuario).all()
        if not usuarios:
            print("No hay usuarios registrados.")
        for u in usuarios:
            print(f"ID: {u.id_usuario} | Nombre: {u.nombre} {u.apellido} | Email: {u.email}")

if __name__ == "__main__":
    UsuarioMenu().menu()
