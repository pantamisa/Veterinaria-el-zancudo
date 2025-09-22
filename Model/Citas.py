from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Crud.Citas_crud import crear_cita, obtener_citas, obtener_cita, actualizar_cita, eliminar_cita
from Citas import menu_usuarios
# ============================
# Configuración de la conexión Neon
# ============================
DATABASE_URL = "postgresql://neondb_owner:npg_MDXR0Zj6mzvY@ep-young-boat-ae7ls9d8-pooler.c-2.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

# Crear motor de conexión
engine = create_engine(DATABASE_URL)

# Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# ============================
# Submenú Citas
# ============================
def menu_citas(db):
    while True:
        print("\n===== SUBMENÚ CITAS =====")
        print("1. Crear Cita")
        print("2. Listar Todas las Citas")
        print("3. Consultar Cita por ID")
        print("4. Actualizar Cita")
        print("5. Eliminar Cita")
        print("0. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_servicio = input("ID del servicio: ")
            id_animal = input("ID del animal: ")
            id_usuario_crea = input("ID del usuario que crea: ")
            fecha_atencion = input("Fecha de atención (YYYY-MM-DD HH:MM, opcional): ") or None
            cita = crear_cita(db, id_servicio, id_animal, id_usuario_crea, fecha_atencion)
            print("Cita creada:", cita)

        elif opcion == "2":
            citas = obtener_citas(db)
            for c in citas:
                print(c)

        elif opcion == "3":
            id_cita = input("ID de la cita: ")
            cita = obtener_cita(db, id_cita)
            print("Cita:", cita if cita else "No encontrada")

        elif opcion == "4":
            id_cita = input("ID de la cita a actualizar: ")
            campo = input("Campo a actualizar (id_servicio, id_animal, fecha_atencion, id_usuario_edita): ")
            valor = input("Nuevo valor: ")
            cita = actualizar_cita(db, id_cita, **{campo: valor})
            print("Cita actualizada:", cita if cita else "No encontrada")

        elif opcion == "5":
            id_cita = input("ID de la cita a eliminar: ")
            cita = eliminar_cita(db, id_cita)
            print("Cita eliminada" if cita else "No encontrada")

        elif opcion == "0":
            break
        else:
            print("Opción inválida")


# ============================
# Menú principal
# ============================
def menu_principal(db):
    while True:
        print("\n========= MENÚ PRINCIPAL =========")
        print("1. Gestión de Usuarios")
        print("2. Gestión de Citas")
        print("0. Salir")
        print("==================================")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_usuarios(db)
        elif opcion == "2":
            menu_citas(db)
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida")

"""
# ============================
# Ejecutar aplicación
# ============================
def main():
    db = SessionLocal()
    try:
        menu_principal(db)
    finally:
        db.close()


if __name__ == "__main__":
    main()
"""