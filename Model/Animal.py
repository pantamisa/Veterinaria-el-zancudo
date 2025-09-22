
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Crud.Animal_crud import AnimalCRUD
from Entities.animal import AnimalCreate, AnimalUpdate, Animal
from Entities.usuario import Usuario
from Entities.Raza_animal import Raza_animal
from Entities.genero import Genero
import uuid

# Configuración de conexión a Neon (PostgreSQL)
DATABASE_URL = 'postgresql://neondb_owner:npg_MDXR0Zj6mzvY@ep-young-boat-ae7ls9d8-pooler.c-2.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class AnimalMenu:
    def __init__(self):
        self.db = SessionLocal()
        self.crud = AnimalCRUD()

    def pedir_uuid(self, mensaje):
        while True:
            valor = input(mensaje)
            try:
                return uuid.UUID(valor)
            except ValueError:
                print("⚠ El valor ingresado no es un UUID válido. Intente de nuevo.")

    def listar_usuarios(self):
        print("\nUsuarios registrados:")
        usuarios = self.db.query(Usuario).all()
        for u in usuarios:
            print(f"ID: {u.id_usuario} | Nombre: {u.nombre} {u.apellido} | Email: {u.email}")

    def listar_generos(self):
        print("\nGéneros registrados:")
        generos = self.db.query(Genero).all()
        for g in generos:
            print(f"ID: {g.id_genero} | Nombre: {g.nombre_genero}")

    def listar_razas(self):
        print("\nRazas registradas:")
        razas = self.db.query(Raza_animal).all()
        for r in razas:
            print(f"ID: {r.id_raza} | Nombre: {r.nombreRaza}")

    def crear_animal(self):
        try:
            print("Antes de crear el animal, consulta los IDs válidos:")
            self.listar_usuarios()
            self.listar_generos()
            self.listar_razas()
            nombre_animal = input("Nombre del animal: ")
            edad_animal = input("Edad del animal: ")
            id_genero = self.pedir_uuid("ID de género (UUID): ")
            id_raza = self.pedir_uuid("ID de raza (UUID): ")
            id_usuario = self.pedir_uuid("ID del propietario (UUID): ")
            id_usuario_crea = self.pedir_uuid("ID del usuario que registra (UUID): ")
            animal_in = AnimalCreate(
                nombre_animal=nombre_animal,
                edad_animal=edad_animal,
                id_genero=id_genero,
                id_raza=id_raza,
                id_usuario=id_usuario,
                id_usuario_crea=id_usuario_crea
            )
            animal = self.crud.create(self.db, animal_in)
            print(f"Animal creado con ID: {animal.id_animal}")
        except Exception as e:
            print(f"Error al crear animal: {e}")
            self.db.rollback()

    def listar_animales(self):
        animales = self.crud.get_all(self.db)
        if not animales:
            print("No hay animales registrados.")
            return
        for a in animales:
            print(f"ID: {a.id_animal} | Nombre: {a.nombre_animal} | Edad: {a.edad_animal} | Género: {a.id_genero} | Raza: {a.id_raza} | Propietario: {a.id_usuario}")

    def ver_animal(self):
        id_animal = self.pedir_uuid("ID del animal (UUID): ")
        animal = self.crud.get(self.db, id_animal)
        if animal:
            print(f"ID: {animal.id_animal}\nNombre: {animal.nombre_animal}\nEdad: {animal.edad_animal}\nGénero: {animal.id_genero}\nRaza: {animal.id_raza}\nPropietario: {animal.id_usuario}")
        else:
            print("Animal no encontrado.")

    def actualizar_animal(self):
        id_animal = self.pedir_uuid("ID del animal a actualizar (UUID): ")
        try:
            print("Deja vacío cualquier campo que no quieras actualizar.")
            nombre_animal = input("Nuevo nombre: ")
            edad_animal = input("Nueva edad: ")
            id_genero = input("Nuevo ID de género (UUID): ")
            id_raza = input("Nuevo ID de raza (UUID): ")
            id_usuario_edita = self.pedir_uuid("ID del usuario que edita (UUID): ")
            animal_in = AnimalUpdate(
                nombre_animal=nombre_animal or None,
                edad_animal=edad_animal or None,
                id_genero=uuid.UUID(id_genero) if id_genero else None,
                id_raza=uuid.UUID(id_raza) if id_raza else None,
                id_usuario_edita=id_usuario_edita
            )
            animal = self.crud.update(self.db, id_animal, animal_in, id_usuario_edita)
            if animal:
                print("Animal actualizado.")
            else:
                print("Animal no encontrado.")
        except Exception as e:
            print(f"Error: {e}")
            self.db.rollback()

    def eliminar_animal(self):
        id_animal = self.pedir_uuid("ID del animal a eliminar (UUID): ")
        ok = self.crud.delete(self.db, id_animal)
        if ok:
            print("Animal eliminado.")
        else:
            print("Animal no encontrado.")

    def menu(self):
        while True:
            print("\n--- MENÚ DE ANIMALES ---")
            print("1. Crear animal")
            print("2. Listar animales")
            print("3. Ver animal por ID")
            print("4. Actualizar animal")
            print("5. Eliminar animal")
            print("6. Listar UUIDs válidos de usuarios, géneros y razas")
            print("0. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.crear_animal()
            elif opcion == "2":
                self.listar_animales()
            elif opcion == "3":
                self.ver_animal()
            elif opcion == "4":
                self.actualizar_animal()
            elif opcion == "5":
                self.eliminar_animal()
            elif opcion == "6":
                self.listar_usuarios()
                self.listar_generos()
                self.listar_razas()
            elif opcion == "0":
                print("Saliendo del menú de animales.")
                break
            else:
                print("Opción no válida.")

if __name__ == "__main__":
    AnimalMenu().menu()