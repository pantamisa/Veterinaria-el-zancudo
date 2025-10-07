# TestConnection.py
from Database.config import SessionLocal, engine, Base, create_tables
from Entities.animal import Animal
from Entities.Citas import Citas
from Entities.genero import Genero
from Entities.Raza_animal import Raza_animal
from Entities.Servicios import Servicios
from Entities.Tipo_animal import Tipo_animal
from Entities.usuario import Usuario
from Model.Menu import MiServicio

def main():
    print("🔄 Intentando conectar con la base de datos Neon...")
    try:
        # Crear tablas en Neon
        create_tables()
        print("✅ Tablas creadas/verificadas en Neon")

        # Abrir sesión
        db = SessionLocal()
        print("✅ Conexión establecida correctamente")

        try:
            # Instanciar tu servicio
            mi_servicio = MiServicio(db=db)
            mi_servicio.Ejecucion()
        finally:
            db.close()
            print("🔒 Sesión cerrada")
    except Exception as e:
        print("❌ Error al conectar o crear tablas en Neon:", e)

if __name__ == "__main__":
    main()
