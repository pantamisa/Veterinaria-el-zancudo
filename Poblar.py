from Database.config import SessionLocal
from Crud.Usuario_crud import create_usuario, login_usuario


db = SessionLocal()

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
