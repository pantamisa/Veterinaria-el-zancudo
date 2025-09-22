import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Crud.Citas_crud import obtener_citas
from Crud.Usuario_crud import get_usuario
from Entities.usuario import Usuario
from Entities.Citas import Citas
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Crud.Factura_crud import crear_factura, obtener_facturas, obtener_factura, marcar_factura_pagada, actualizar_costo_factura, eliminar_factura
import uuid

# Configuración de conexión a Neon (PostgreSQL)
DATABASE_URL = 'postgresql://neondb_owner:npg_MDXR0Zj6mzvY@ep-young-boat-ae7ls9d8-pooler.c-2.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Factura:
    def listar_citas(self):
        print("\nCitas registradas:")
        citas = self.db.query(Citas).all()
        if not citas:
            print("No hay citas registradas.")
        for c in citas:
            print(f"ID: {c.id_citas} | Animal: {c.id_animal} | Servicio: {c.id_servicio} | Fecha: {c.fecha_asignacion}")

    def listar_usuarios(self):
        print("\nUsuarios registrados:")
        usuarios = self.db.query(Usuario).all()
        if not usuarios:
            print("No hay usuarios registrados.")
        for u in usuarios:
            print(f"ID: {u.id_usuario} | Nombre: {u.nombre} {u.apellido} | Email: {u.email}")
    def __init__(self):
        self.db = SessionLocal()

    def menu(self):
        while True:
            print("\n--- MENÚ DE FACTURAS ---")
            print("1. Crear factura")
            print("2. Listar facturas")
            print("3. Ver factura por ID")
            print("4. Marcar factura como pagada")
            print("5. Actualizar costo de factura")
            print("6. Eliminar factura")
            print("7. Listar UUIDs válidos de citas y usuarios")
            print("0. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.crear_factura()
            elif opcion == "2":
                self.listar_facturas()
            elif opcion == "3":
                self.ver_factura()
            elif opcion == "4":
                self.pagar_factura()
            elif opcion == "5":
                self.actualizar_costo()
            elif opcion == "6":
                self.eliminar_factura()
            elif opcion == "7":
                print("\n--- UUIDs válidos de Citas ---")
                self.listar_citas()
                print("\n--- UUIDs válidos de Usuarios ---")
                self.listar_usuarios()
            elif opcion == "0":
                print("Saliendo del menú de facturas.")
                break
            else:
                print("Opción no válida.")

    def pedir_uuid(self, mensaje):
        import uuid
        while True:
            valor = input(mensaje)
            try:
                return str(uuid.UUID(valor))
            except ValueError:
                print("⚠ El valor ingresado no es un UUID válido. Intente de nuevo.")

    def crear_factura(self):
        try:
            print("\nAntes de crear la factura, puedes consultar los IDs válidos:")
            self.listar_citas()
            self.listar_usuarios()
            id_cita = self.pedir_uuid("ID de la cita (UUID): ")
            costo = float(input("Costo: "))
            id_usuario_pago = self.pedir_uuid("ID usuario que paga (UUID): ")
            factura = crear_factura(self.db, id_cita, costo, id_usuario_pago)
            print(f"Factura creada con ID: {factura.id_factura}")
        except Exception as e:
            print(f"Error al crear factura: {e}")
            self.db.rollback()

    def listar_facturas(self):
        facturas = obtener_facturas(self.db)
        if not facturas:
            print("No hay facturas registradas.")
            return
        for f in facturas:
            print(f"ID: {f.id_factura} | Costo: {f.costo} | Pagada: {f.pagada} | Fecha generación: {f.fecha_generacion} | Fecha pago: {f.fecha_pago}")

    def ver_factura(self):
        id_factura = self.pedir_uuid("ID de la factura (UUID): ")
        factura = obtener_factura(self.db, id_factura)
        if factura:
            print(f"ID: {factura.id_factura}\nCosto: {factura.costo}\nPagada: {factura.pagada}\nFecha generación: {factura.fecha_generacion}\nFecha pago: {factura.fecha_pago}")
        else:
            print("Factura no encontrada.")

    def pagar_factura(self):
        id_factura = self.pedir_uuid("ID de la factura a marcar como pagada (UUID): ")
        factura = marcar_factura_pagada(self.db, id_factura)
        if factura:
            print(f"Factura marcada como pagada.\nID: {factura.id_factura}\nPagada: {factura.pagada}\nFecha pago: {factura.fecha_pago}")
        else:
            print("Factura no encontrada o ya estaba pagada.")

    def actualizar_costo(self):
        id_factura = self.pedir_uuid("ID de la factura a actualizar (UUID): ")
        try:
            nuevo_costo = float(input("Nuevo costo: "))
            factura = actualizar_costo_factura(self.db, id_factura, nuevo_costo)
            if factura:
                print("Costo actualizado.")
            else:
                print("Factura no encontrada.")
        except Exception as e:
            print(f"Error: {e}")
            self.db.rollback()

    def eliminar_factura(self):
        id_factura = self.pedir_uuid("ID de la factura a eliminar (UUID): ")
        factura = eliminar_factura(self.db, id_factura)
        if factura:
            print("Factura eliminada.")
        else:
            print("Factura no encontrada.")

if __name__ == "__main__":
    Factura().menu()