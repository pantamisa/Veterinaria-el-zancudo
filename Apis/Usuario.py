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
    create_usuario,
    get_usuario,
    update_usuario,
    delete_usuario,
    login_usuario,
    contar_usuarios
)
from Entities.usuario import Usuario

from Schemas import (
    UsuarioCreate,
    UsuarioUpdate,
    UsuarioResponse,
    CambioContraseña,
    RespuestaAPI
)

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


# Dependency para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==================== ENDPOINTS GET ====================


@router.get("/total")
def obtener_total_usuarios(db: Session = Depends(get_db)):
    try:
        total = contar_usuarios(db)
        return {"total_usuarios": total}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al contar usuarios: {str(e)}"
        )
    
@router.get("/", response_model=List[UsuarioResponse])
async def obtener_usuarios(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Obtener todos los usuarios con paginación.
    
    - **skip**: Número de registros a saltar (paginación)
    - **limit**: Número máximo de registros a devolver
    """
    try:
        usuarios = db.query(Usuario).offset(skip).limit(limit).all()
        return usuarios
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener usuarios: {str(e)}"
        )


@router.get("/{usuario_id}", response_model=UsuarioResponse)
async def obtener_usuario_por_id(
    usuario_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Obtener un usuario específico por su ID.
    
    - **usuario_id**: UUID del usuario a buscar
    """
    try:
        usuario = get_usuario(db, usuario_id)
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no encontrado"
            )
        return usuario
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener usuario: {str(e)}"
        )


@router.get("/email/{email}", response_model=UsuarioResponse)
async def obtener_usuario_por_email(
    email: str,
    db: Session = Depends(get_db)
):
    """
    Obtener un usuario por su email.
    
    - **email**: Email del usuario a buscar
    """
    try:
        usuario = db.query(Usuario).filter(Usuario.email == email).first()
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no encontrado"
            )
        return usuario
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener usuario: {str(e)}"
        )


@router.get("/admin/lista", response_model=List[UsuarioResponse])
async def obtener_usuarios_admin(db: Session = Depends(get_db)):
    """
    Obtener todos los usuarios que son administradores.
    """
    try:
        admins = db.query(Usuario).filter(Usuario.es_admin == True).all()
        return admins
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener administradores: {str(e)}"
        )


# ==================== ENDPOINTS POST ====================

@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
async def crear_usuario(
    usuario_data: UsuarioCreate,
    db: Session = Depends(get_db)
):
    """
    Crear un nuevo usuario en el sistema.
    
    - **nombre**: Nombre del usuario
    - **apellido**: Apellido del usuario
    - **email**: Email único del usuario
    - **telefono**: Teléfono de contacto (opcional)
    - **password**: Contraseña (será hasheada automáticamente)
    - **es_admin**: Si el usuario es administrador (default: False)
    """
    try:
        # Verificar si el email ya existe
        usuario_existente = db.query(Usuario).filter(Usuario.email == usuario_data.email).first()
        if usuario_existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El email ya está registrado"
            )
        
        # Crear el usuario
        nuevo_usuario = create_usuario(
            db=db,
            nombre=usuario_data.nombre,
            apellido=usuario_data.apellido,
            email=usuario_data.email,
            telefono=usuario_data.telefono,
            password=usuario_data.password,
            es_admin=usuario_data.es_admin
        )
        
        return nuevo_usuario
        
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al crear usuario: {str(e)}"
        )

        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al iniciar sesión: {str(e)}"
        )


@router.post("/{usuario_id}/cambiar-contrasena", response_model=RespuestaAPI)
async def cambiar_contrasena(
    usuario_id: UUID,
    cambio_data: CambioContraseña,
    db: Session = Depends(get_db)
):
    """
    Cambiar la contraseña de un usuario.
    
    - **usuario_id**: UUID del usuario
    - **contraseña_actual**: Contraseña actual del usuario
    - **nueva_contraseña**: Nueva contraseña deseada
    """
    try:
        # Verificar que el usuario existe
        usuario = get_usuario(db, usuario_id)
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no encontrado"
            )
        
        # Verificar la contraseña actual
        usuario_valido = login_usuario(db, usuario.email, cambio_data.contraseña_actual)
        if not usuario_valido:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="La contraseña actual es incorrecta"
            )
        
        # Actualizar con la nueva contraseña
        update_usuario(db, usuario_id, password=cambio_data.nueva_contraseña)
        
        return RespuestaAPI(
            mensaje="Contraseña cambiada exitosamente",
            exito=True
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al cambiar contraseña: {str(e)}"
        )


# ==================== ENDPOINTS PUT/PATCH ====================

@router.put("/{usuario_id}", response_model=UsuarioResponse)
async def actualizar_usuario_completo(
    usuario_id: UUID,
    usuario_data: UsuarioUpdate,
    db: Session = Depends(get_db)
):
    """
    Actualizar información de un usuario.
    
    - **usuario_id**: UUID del usuario a actualizar
    - Solo se actualizarán los campos proporcionados (parcial update)
    """
    try:
        # Verificar que el usuario existe
        usuario_existente = get_usuario(db, usuario_id)
        if not usuario_existente:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no encontrado"
            )
        
        # Filtrar solo los campos que tienen valor
        campos_actualizacion = {
            k: v for k, v in usuario_data.dict(exclude_unset=True).items()
            if v is not None
        }
        
        if not campos_actualizacion:
            return usuario_existente
        
        # Si se intenta actualizar el email, verificar que no exista
        if 'email' in campos_actualizacion:
            email_existente = db.query(Usuario).filter(
                Usuario.email == campos_actualizacion['email'],
                Usuario.id_usuario != usuario_id
            ).first()
            if email_existente:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="El email ya está en uso por otro usuario"
                )
        
        # Actualizar usuario
        usuario_actualizado = update_usuario(db, usuario_id, **campos_actualizacion)
        
        return usuario_actualizado
        
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al actualizar usuario: {str(e)}"
        )


# ==================== ENDPOINTS DELETE ====================

@router.delete("/{usuario_id}", response_model=RespuestaAPI)
async def eliminar_usuario_endpoint(
    usuario_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Eliminar un usuario del sistema.
    
    ⚠️ ADVERTENCIA: Esta acción eliminará o modificará todos los datos relacionados:
    - Facturas asociadas serán eliminadas
    - Animales del propietario serán eliminados
    - Citas asociadas serán eliminadas por cascade
    
    - **usuario_id**: UUID del usuario a eliminar
    """
    try:
        # Verificar que el usuario existe
        usuario_existente = get_usuario(db, usuario_id)
        if not usuario_existente:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no encontrado"
            )
        
        # Eliminar usuario (maneja las relaciones internamente)
        eliminado = delete_usuario(db, usuario_id)
        
        if eliminado:
            return RespuestaAPI(
                mensaje="Usuario eliminado exitosamente",
                exito=True,
                datos={"id_eliminado": str(usuario_id)}
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error al eliminar usuario"
            )
            
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al eliminar usuario: {str(e)}"
        )


# ==================== ENDPOINTS ADICIONALES ====================

@router.get("/{usuario_id}/es-admin", response_model=RespuestaAPI)
async def verificar_es_admin(
    usuario_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Verificar si un usuario tiene permisos de administrador.
    
    - **usuario_id**: UUID del usuario a verificar
    """
    try:
        usuario = get_usuario(db, usuario_id)
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no encontrado"
            )
        
        return RespuestaAPI(
            mensaje=f"El usuario {'es' if usuario.es_admin else 'no es'} administrador",
            exito=True,
            datos={"es_admin": usuario.es_admin}
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al verificar administrador: {str(e)}"
        )


@router.get("/{usuario_id}/animales", response_model=RespuestaAPI)
async def obtener_animales_usuario(
    usuario_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Obtener todos los animales registrados para un usuario específico.
    
    - **usuario_id**: UUID del propietario
    """
    try:
        from Entities.animal import Animal
        
        usuario = get_usuario(db, usuario_id)
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no encontrado"
            )
        
        animales = db.query(Animal).filter(Animal.id_usuario == usuario_id).all()
        
        animales_data = [
            {
                "id_animal": str(a.id_animal),
                "nombre_animal": a.nombre_animal,
                "edad_animal": a.edad_animal
            }
            for a in animales
        ]
        
        return RespuestaAPI(
            mensaje=f"Se encontraron {len(animales)} animales",
            exito=True,
            datos={"total": len(animales), "animales": animales_data}
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener animales: {str(e)}"
        )