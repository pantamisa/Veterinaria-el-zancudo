
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Crud.Citas_crud import crear_cita, obtener_citas, obtener_cita, actualizar_cita, eliminar_cita
from Entities.Citas import Citas
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuración de conexión a Neon (PostgreSQL)
DATABASE_URL = 'postgresql://neondb_owner:npg_MDXR0Zj6mzvY@ep-young-boat-ae7ls9d8-pooler.c-2.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


import uuid

class CitasMenu:
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
            print("\n===== SUBMENÚ CITAS =====")
            print("1. Crear Cita")
            print("2. Listar Todas las Citas")
            print("3. Consultar Cita por ID")
            print("4. Actualizar Cita")
            print("5. Eliminar Cita")
            print("6. Listar Citas (detallado)")
            print("0. Volver al Menú Principal")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear_cita()
            elif opcion == "2":
                self.listar_citas()
            elif opcion == "3":
                self.consultar_cita()
            elif opcion == "4":
                self.actualizar_cita()
            elif opcion == "5":
                self.eliminar_cita()
            elif opcion == "6":
                self.listar_citas_detallado()
            elif opcion == "0":
                print("Volviendo al menú principal...")
                break
            else:
                print("Opción no válida.")

    def crear_cita(self):
        try:
            id_servicio = self.pedir_uuid("ID del servicio (UUID): ")
            id_animal = self.pedir_uuid("ID del animal (UUID): ")
            id_usuario_crea = self.pedir_uuid("ID del usuario que crea (UUID): ")
            fecha_atencion = input("Fecha de atención (YYYY-MM-DD HH:MM, opcional): ") or None
            cita = crear_cita(self.db, id_servicio, id_animal, id_usuario_crea, fecha_atencion)
            print("Cita creada:", cita)
        except Exception as e:
            print(f"Error al crear cita: {e}")
            self.db.rollback()

    def listar_citas(self):
        citas = obtener_citas(self.db)
        if not citas:
            print("No hay citas registradas.")
            return
        for c in citas:
            print(c)

    def consultar_cita(self):
        id_cita = self.pedir_uuid("ID de la cita (UUID): ")
        cita = obtener_cita(self.db, id_cita)
        print("Cita:", cita if cita else "No encontrada")

    def actualizar_cita(self):
        id_cita = self.pedir_uuid("ID de la cita a actualizar (UUID): ")
        campo = input("Campo a actualizar (id_servicio, id_animal, fecha_atencion, id_usuario_edita): ")
        valor = input("Nuevo valor: ")
        cita = actualizar_cita(self.db, id_cita, **{campo: valor})
        print("Cita actualizada:", cita if cita else "No encontrada")

    def eliminar_cita(self):
        id_cita = self.pedir_uuid("ID de la cita a eliminar (UUID): ")
        cita = eliminar_cita(self.db, id_cita)
        print("Cita eliminada" if cita else "No encontrada")

    def listar_citas_detallado(self):
        citas = self.db.query(Citas).all()
        if not citas:
            print("No hay citas registradas.")
        for c in citas:
            print(f"ID: {c.id_citas} | Animal: {c.id_animal} | Servicio: {c.id_servicio} | Fecha: {c.fecha_asignacion}")

if __name__ == "__main__":
    CitasMenu().menu()

