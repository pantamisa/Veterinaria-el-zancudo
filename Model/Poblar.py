# Poblar.py - Versión completa
from Database.config import SessionLocal, Base, engine
from Entities.genero import Genero
from Entities.Servicios import Servicios
from Entities.Tipo_animal import Tipo_animal
from Entities.Raza_animal import Raza_animal
from Crud.Usuario_crud import create_usuario, login_usuario

# Importar todos los modelos para que SQLAlchemy los reconozca
from Entities.usuario import Usuario
from Entities.animal import Animal
from Entities.Citas import Citas
from Entities.Factura import Factura
from Crud.Citas_crud import crear_cita
from datetime import datetime, timedelta



def crear_cita_ejemplo():
    """Crear una cita de ejemplo usando datos existentes"""
    db = SessionLocal()
    
    try:
        # Verificar que existan los datos necesarios
        animales = db.query(Animal).all()
        servicios = db.query(Servicios).all()
        usuarios = db.query(Usuario).all()
        
        if not animales:
            print("Error: No hay animales registrados. Crea animales primero.")
            return None
        
        if not servicios:
            print("Error: No hay servicios registrados. Crea servicios primero.")
            return None
            
        if not usuarios:
            print("Error: No hay usuarios registrados. Crea usuarios primero.")
            return None
        
        # Seleccionar datos para la cita
        animal_seleccionado = animales[0]  # Primer animal
        servicio_seleccionado = servicios[0]  # Primer servicio
        usuario_creador = usuarios[-1]  # Último usuario como quien crea la cita
        
        # Fecha de atención para mañana
        fecha_atencion = datetime.now() + timedelta(days=1)
        
        print(f"Creando cita para:")
        print(f"Animal: {animal_seleccionado.nombre_animal}")
        print(f"Servicio: {servicio_seleccionado.nombre_ser}")
        print(f"Costo: ${servicio_seleccionado.costo:,.0f}")
        print(f"Fecha programada: {fecha_atencion.strftime('%Y-%m-%d %H:%M')}")
        
        # Crear la cita
        nueva_cita = crear_cita(
            db=db,
            id_servicio=servicio_seleccionado.id_servicio,
            id_animal=animal_seleccionado.id_animal,
            id_usuario_crea=usuario_creador.id_usuario,
            fecha_atencion=fecha_atencion
        )
        
        if nueva_cita:
            print(f"Cita creada exitosamente!")
            print(f"ID de la cita: {nueva_cita.id_citas}")
            print(f"Fecha de asignación: {nueva_cita.fecha_asignacion}")
            return nueva_cita
        else:
            print("Error al crear la cita")
            return None
        
    except Exception as e:
        print(f"Error al crear cita: {e}")
        db.rollback()
        return None
    finally:
        db.close()

def crear_animales_prueba():
    """Crear 5 animales de prueba para la veterinaria"""
    db = SessionLocal()
    
    try:
        # Primero verificar que existan los datos necesarios
        usuarios = db.query(Usuario).all()
        generos = db.query(Genero).all()
        razas = db.query(Raza_animal).all()
        
        if not usuarios:
            print("Error: No hay usuarios registrados. Crea usuarios primero.")
            return []
        
        if not generos:
            print("Error: No hay géneros registrados. Ejecuta CrearGeneros() primero.")
            return []
            
        if not razas:
            print("Error: No hay razas registradas. Ejecuta CrearTiposYRazas() primero.")
            return []
        
        # Obtener IDs necesarios
        usuario_propietario = usuarios[0]  # Primer usuario como propietario
        usuario_creador = usuarios[-1] if len(usuarios) > 1 else usuarios[0]  # Último usuario como creador
        
        genero_macho = next((g for g in generos if g.nombre_genero == "Macho"), generos[0])
        genero_hembra = next((g for g in generos if g.nombre_genero == "Hembra"), generos[0])
        
        # Datos de los 5 animales
        animales_data = [
            {
                "nombre_animal": "Max",
                "edad_animal": "3",
                "genero": genero_macho,
                "raza": next((r for r in razas if "Labrador" in r.nombreRaza), razas[0])
            },
            {
                "nombre_animal": "Luna",
                "edad_animal": "2",
                "genero": genero_hembra,
                "raza": next((r for r in razas if "Persa" in r.nombreRaza), razas[0])
            },
            {
                "nombre_animal": "Rocky",
                "edad_animal": "5",
                "genero": genero_macho,
                "raza": next((r for r in razas if "Pastor" in r.nombreRaza), razas[0])
            },
            {
                "nombre_animal": "Bella",
                "edad_animal": "1",
                "genero": genero_hembra,
                "raza": next((r for r in razas if "Golden" in r.nombreRaza), razas[0])
            },
            {
                "nombre_animal": "Pipo",
                "edad_animal": "4",
                "genero": genero_macho,
                "raza": next((r for r in razas if "Canario" in r.nombreRaza), razas[0])
            }
        ]
        
        animales_creados = []
        
        for animal_info in animales_data:
            # Verificar si el animal ya existe
            animal_existente = db.query(Animal).filter(
                Animal.nombre_animal == animal_info["nombre_animal"]
            ).first()
            
            if animal_existente:
                print(f"El animal {animal_info['nombre_animal']} ya existe")
                animales_creados.append(animal_existente)
                continue
            
            # Crear nuevo animal
            nuevo_animal = Animal(
                nombre_animal=animal_info["nombre_animal"],
                edad_animal=animal_info["edad_animal"],
                id_usuario=usuario_propietario.id_usuario,
                id_genero=animal_info["genero"].id_genero,
                id_raza=animal_info["raza"].id_raza,
                id_usuario_crea=usuario_creador.id_usuario
            )
            
            db.add(nuevo_animal)
            animales_creados.append(nuevo_animal)
        
        # Confirmar cambios
        db.commit()
        
        # Refrescar objetos para obtener los IDs generados
        for animal in animales_creados:
            if animal not in db.query(Animal).all():
                db.refresh(animal)
        
        print("Animales procesados correctamente:")
        print("=" * 60)
        
        for animal in animales_creados:
            # Cargar relaciones para mostrar información completa
            db.refresh(animal)
            print(f"Nombre: {animal.nombre_animal}")
            print(f"Edad: {animal.edad_animal} años")
            print(f"Género: {animal.genero.nombre_genero}")
            print(f"Raza: {animal.raza.nombreRaza}")
            print(f"Tipo: {animal.raza.tipo_animal.nombre}")
            print(f"Propietario: {animal.usuario_propietario.nombre} {animal.usuario_propietario.apellido}")
            print(f"ID: {animal.id_animal}")
            print("-" * 60)
        
        print(f"Total animales: {len(animales_creados)}")
        return animales_creados
        
    except Exception as e:
        print(f"Error al crear animales: {e}")
        db.rollback()
        return []
    finally:
        db.close()

def crear_usuarios_adicionales():
    """Crear 2 usuarios adicionales para la veterinaria"""
    db = SessionLocal()
    
    usuarios_data = [
        {
            "nombre": "María",
            "apellido": "González",
            "email": "maria.gonzalez@veterinaria.com",
            "telefono": "3001234567",
            "password": "maria123",
            "es_admin": True  # Usuario administrador
        },
        {
            "nombre": "Carlos",
            "apellido": "Rodríguez",
            "email": "carlos.rodriguez@cliente.com",
            "telefono": "3109876543",
            "password": "carlos456",
            "es_admin": False  # Cliente regular
        }
    ]
    
    usuarios_creados = []
    
    try:
        for usuario_info in usuarios_data:
            # Verificar si el usuario ya existe
            usuario_existente = db.query(Usuario).filter(
                Usuario.email == usuario_info["email"]
            ).first()
            
            if usuario_existente:
                print(f"El usuario {usuario_info['email']} ya existe")
                usuarios_creados.append(usuario_existente)
                continue
            
            # Crear nuevo usuario
            nuevo_usuario = create_usuario(
                db,
                nombre=usuario_info["nombre"],
                apellido=usuario_info["apellido"],
                email=usuario_info["email"],
                telefono=usuario_info["telefono"],
                password=usuario_info["password"],
                es_admin=usuario_info["es_admin"]
            )
            
            usuarios_creados.append(nuevo_usuario)
            
            rol = "Administrador" if nuevo_usuario.es_admin else "Cliente"
            print(f"Usuario creado: {nuevo_usuario.nombre} {nuevo_usuario.apellido} ({rol})")
            print(f"  Email: {nuevo_usuario.email}")
            print(f"  Teléfono: {nuevo_usuario.telefono}")
            print(f"  ID: {nuevo_usuario.id_usuario}")
            print("-" * 50)
        
        print(f"Total usuarios procesados: {len(usuarios_creados)}")
        return usuarios_creados
        
    except Exception as e:
        print(f"Error al crear usuarios: {e}")
        db.rollback()
        return []
    finally:
        db.close()

def crear_tablas_si_no_existen():
    """Crea las tablas si no existen"""
    try:
        from sqlalchemy import inspect
        inspector = inspect(engine)
        tablas_existentes = inspector.get_table_names()
        
        if not tablas_existentes or 'servicios' not in tablas_existentes:
            print("Creando tablas en la base de datos...")
            Base.metadata.create_all(bind=engine)
            print("✅ Tablas creadas exitosamente")
        else:
            print("✅ Las tablas ya existen")
            
    except Exception as e:
        print(f"❌ Error al verificar/crear tablas: {e}")
        return False
    return True

def CrearUsuarioPrueba():
    """Crear usuario de prueba con manejo de sesión"""
    db = SessionLocal()
    try:
        # Verificar si el usuario ya existe
        usuario_existente = db.query(Usuario).filter(Usuario.email == "kelvin@example.com").first()
        if usuario_existente:
            print("✅ El usuario de prueba ya existe")
            return usuario_existente

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

        # Login de prueba
        usuario_login = login_usuario(db, "kelvin@example.com", "miClaveSegura")
        if usuario_login:
            print("✅ Login correcto:", usuario_login.nombre)
        else:
            print("❌ Credenciales incorrectas")
            
        return nuevo

    except Exception as e:
        print(f"❌ Error al crear usuario: {e}")
        db.rollback()
        return None
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
        generos = [
            Genero(nombre_genero="Macho"),
            Genero(nombre_genero="Hembra"),
            Genero(nombre_genero="Otro")
        ]

        # Agregar a la sesión
        db.add_all(generos)
        db.commit()

        # Refrescar para ver los UUID generados
        for genero in generos:
            db.refresh(genero)

        print("✅ Géneros insertados correctamente")
        for genero in generos:
            print(f"- {genero.nombre_genero} ID: {genero.id_genero}")

    except Exception as e:
        db.rollback()
        print("❌ Error al poblar tabla Género:", e)
    finally:
        db.close()

def CrearServicios():
    """Crear servicios veterinarios básicos"""
    db = SessionLocal()
    try:
        # Verificar si ya existen servicios
        servicios_existentes = db.query(Servicios).count()
        if servicios_existentes > 0:
            print("✅ Los servicios ya existen en la base de datos")
            return

        # Definir servicios iniciales
        servicios_data = [
            {"nombre_ser": "Baño", "costo": 15000.0},
            {"nombre_ser": "Vacunas", "costo": 100000.0},
            {"nombre_ser": "Desparasitar", "costo": 200000.0}
        ]
        
        servicios_creados = []
        
        # Crear cada servicio
        for servicio_info in servicios_data:
            nuevo_servicio = Servicios(
                nombre_ser=servicio_info["nombre_ser"],
                costo=servicio_info["costo"]
            )
            db.add(nuevo_servicio)
            servicios_creados.append(nuevo_servicio)
        
        # Confirmar cambios
        db.commit()
        
        # Refrescar objetos para obtener los IDs generados
        for servicio in servicios_creados:
            db.refresh(servicio)
        
        print("✅ Servicios insertados correctamente:")
        for servicio in servicios_creados:
            print(f"- {servicio.nombre_ser}: ${servicio.costo:,.0f}")
        
        return servicios_creados
        
    except Exception as e:
        db.rollback()
        print(f"❌ Error al poblar servicios: {e}")
        return None
    finally:
        db.close()

def CrearTiposYRazas():
    """Crear tipos de animales y razas básicas"""
    db = SessionLocal()
    try:
        # Verificar si ya existen tipos
        tipos_existentes = db.query(Tipo_animal).count()
        if tipos_existentes > 0:
            print("✅ Los tipos de animales ya existen")
            return

        # Crear tipos de animales
        tipos_data = [
            {"nombre": "Perro", "razas": ["Labrador", "Golden Retriever", "Pastor Alemán", "Bulldog"]},
            {"nombre": "Gato", "razas": ["Persa", "Siamés", "Maine Coon", "Británico"]},
            {"nombre": "Ave", "razas": ["Canario", "Periquito", "Cacatúa", "Loro"]}
        ]

        for tipo_info in tipos_data:
            # Crear tipo de animal
            nuevo_tipo = Tipo_animal(nombre=tipo_info["nombre"])
            db.add(nuevo_tipo)
            db.flush()  # Para obtener el ID antes del commit
            
            # Crear razas para este tipo
            for raza_nombre in tipo_info["razas"]:
                nueva_raza = Raza_animal(
                    nombreRaza=raza_nombre,
                    id_tipoAnimal=nuevo_tipo.id_tipoAnimal
                )
                db.add(nueva_raza)
        
        db.commit()
        print("✅ Tipos de animales y razas creados correctamente")
        
        # Mostrar resumen
        tipos = db.query(Tipo_animal).all()
        for tipo in tipos:
            razas_count = len(tipo.razas)
            print(f"- {tipo.nombre}: {razas_count} razas")
            
    except Exception as e:
        db.rollback()
        print(f"❌ Error al crear tipos y razas: {e}")
    finally:
        db.close()

def CrearUsuarioPrueba02():
    """Crear usuario de prueba con manejo de sesión"""
    db = SessionLocal()
    try:
        # Verificar si el usuario ya existe
        usuario_existente = db.query(Usuario).filter(Usuario.email == "Admin@admin.com").first()
        if usuario_existente:
            print("✅ El usuario de prueba ya existe")
            return usuario_existente

        # Crear usuario
        nuevo = create_usuario(
            db,
            nombre="Admin",
            apellido="_____", 
            email="Admin@admin.com",
            telefono="123456",
            password="abc1234",
            es_admin=True
        )

        print("Usuario creado:", nuevo.to_dict())

        # Login de prueba
        usuario_login = login_usuario(db, "Admin@admin.com", "abc1234")
        if usuario_login:
            print("✅ Login correcto:", usuario_login.nombre)
        else:
            print("❌ Credenciales incorrectas")
            
        return nuevo

    except Exception as e:
        print(f"❌ Error al crear usuario: {e}")
        db.rollback()
        return None
    finally:
        db.close()

def poblar_datos_iniciales():
    """Función principal para poblar todos los datos iniciales"""
    print("🔄 Iniciando población de datos...")
    
    # 1. Crear tablas si no existen
    if not crear_tablas_si_no_existen():
        print("❌ Error al crear tablas. Abortando...")
        return
    
    # 2. Poblar datos básicos
    #CrearGeneros()
    #CrearServicios()
    #CrearTiposYRazas()
    #CrearUsuarioPrueba()
    #crear_usuarios_adicionales()
    #crear_animales_prueba()
    #crear_cita_ejemplo()
    CrearUsuarioPrueba02()
    print("✅ Población de datos completada exitosamente")

if __name__ == "__main__":

    poblar_datos_iniciales()