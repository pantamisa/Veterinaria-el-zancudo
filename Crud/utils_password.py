from passlib.context import CryptContext

# Configuramos bcrypt como esquema por defecto
pwd_context = CryptContext(
    schemes=["bcrypt"],
    default="bcrypt",        # 👈 establece bcrypt como predeterminado
    deprecated="auto"
)

def hash_password(password: str) -> str:
    """Hashea la contraseña usando bcrypt."""
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    """Verifica una contraseña contra un hash."""
    return pwd_context.verify(password, hashed)