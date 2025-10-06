"""aca van los usuarios"""

"""
API de Usuarios - Endpoints para gestión de usuarios
Veterinaria El Zancudo
"""
from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from Database.config import SessionLocal
from Crud.Usuario_crud import (
    login_usuario
)
from Entities.usuario import Usuario

from Schemas import (
    UsuarioLogin,
    LoginResponse,
)

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


"""# Dependency para obtener la sesión de base de datos"""
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/login", response_model=LoginResponse)
async def login(
    credentials: UsuarioLogin,
    db: Session = Depends(get_db)
):
    """
    Iniciar sesión con email y contraseña.
    
    - **email**: Email del usuario
    - **password**: Contraseña del usuario
    """
    try:
        usuario = login_usuario(db, credentials.email, credentials.password)

        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales inválidas"
            )

        """# En producción, aquí generarías un token JWT"""
        token_simulado = f"token_{usuario.id_usuario}"

        return LoginResponse(
            token=token_simulado,
            usuario=usuario
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al iniciar sesión: {str(e)}"
        )


    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener animales: {str(e)}"
        )