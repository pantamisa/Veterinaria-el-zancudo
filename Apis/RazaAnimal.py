""" api_razas_animal.py"""
from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from Database.config import SessionLocal
from Crud.Razaanimal_crud import RazaAnimalCRUD

from Schemas import (
    RazaAnimalCreate,
    RazaAnimalUpdate,
    RazaAnimalResponse,
    RazaAnimalConTipo,
    RespuestaAPI
)

router = APIRouter(prefix="/razas-animal", tags=["Razas de Animales"])

"""# Dependency para obtener la sesión de base de datos"""
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""# ==================== ENDPOINTS GET ===================="""

@router.get("/", response_model=List[RazaAnimalResponse])
async def obtener_razas(
    skip: int = 0,
    limit: int = 100,
    id_tipoAnimal: Optional[UUID] = Query(None, description="Filtrar por tipo de animal"),
    db: Session = Depends(get_db)
):
    """
    Obtener todas las razas de animales con paginación y filtros.
    
    - **skip**: Número de registros a saltar (paginación)
    - **limit**: Número máximo de registros a devolver
    - **id_tipoAnimal**: Filtrar por tipo de animal específico
    """
    try:
        crud = RazaAnimalCRUD(db)
        
        if id_tipoAnimal:
            razas = crud.obtener_razas_por_tipo(id_tipoAnimal, skip, limit)
        else:
            razas = crud.obtener_razas(skip, limit)
        
        return razas
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener razas: {str(e)}"
        )

@router.get("/{raza_id}", response_model=RazaAnimalResponse)
async def obtener_raza_por_id(
    raza_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Obtener una raza específica por su ID.
    
    - **raza_id**: UUID de la raza a buscar
    """
    try:
        crud = RazaAnimalCRUD(db)
        raza = crud.obtener_raza(raza_id)
        
        if not raza:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Raza no encontrada"
            )
        
        return raza
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener raza: {str(e)}"
        )

@router.get("/nombre/{nombre_raza}", response_model=RazaAnimalResponse)
async def obtener_raza_por_nombre(
    nombre_raza: str,
    db: Session = Depends(get_db)
):
    """
    Obtener una raza por su nombre (búsqueda exacta).
    
    - **nombre_raza**: Nombre exacto de la raza a buscar
    """
    try:
        crud = RazaAnimalCRUD(db)
        raza = crud.obtener_raza_por_nombre(nombre_raza)
        
        if not raza:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Raza no encontrada"
            )
        
        return raza
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener raza: {str(e)}"
        )

@router.get("/buscar/{termino}", response_model=List[RazaAnimalResponse])
async def buscar_razas(
    termino: str,
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db)
):
    """
    Buscar razas por término (búsqueda parcial en el nombre).
    
    - **termino**: Término de búsqueda
    - **skip**: Número de registros a saltar
    - **limit**: Número máximo de resultados
    """
    try:
        # Para búsqueda parcial, necesitamos extender el CRUD o hacer la consulta directa
        from Entities.Raza_animal import Raza_animal
        razas = db.query(Raza_animal).filter(
            Raza_animal.nombreRaza.ilike(f"%{termino}%")
        ).offset(skip).limit(limit).all()
        
        return razas
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al buscar razas: {str(e)}"
        )

""" ENDPOINTS POST"""

@router.post("/", response_model=RazaAnimalResponse, status_code=status.HTTP_201_CREATED)
async def crear_raza(
    raza_data: RazaAnimalCreate,
    db: Session = Depends(get_db)
):
    """
    Crear una nueva raza de animal en el sistema.
    
    - **nombreRaza**: Nombre único de la raza
    - **id_tipoAnimal**: ID del tipo de animal al que pertenece
    """
    try:
        # Verificar si el tipo de animal existe
        from Entities.Tipo_animal import Tipo_animal
        tipo_animal = db.query(Tipo_animal).filter(
            Tipo_animal.id_tipoAnimal == raza_data.id_tipoAnimal
        ).first()
        
        if not tipo_animal:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El tipo de animal especificado no existe"
            )
        
        # Verificar si la raza ya existe (mismo nombre)
        crud = RazaAnimalCRUD(db)
        raza_existente = crud.obtener_raza_por_nombre(raza_data.nombreRaza)
        
        if raza_existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe una raza con ese nombre"
            )
        
        # Crear la nueva raza usando el CRUD
        nueva_raza = crud.crear_raza_animal(
            nombreRaza=raza_data.nombreRaza,
            id_tipoAnimal=raza_data.id_tipoAnimal
        )
        
        return nueva_raza
        
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al crear raza: {str(e)}"
        )

"""ENDPOINTS PUT/PATCH """

@router.put("/{raza_id}", response_model=RazaAnimalResponse)
async def actualizar_raza(
    raza_id: UUID,
    raza_data: RazaAnimalUpdate,
    db: Session = Depends(get_db)
):
    """
    Actualizar información de una raza de animal.
    
    - **raza_id**: UUID de la raza a actualizar
    - Solo se actualizarán los campos proporcionados
    """
    try:
        crud = RazaAnimalCRUD(db)
        
        """# Verificar que la raza existe"""
        raza_existente = crud.obtener_raza(raza_id)
        if not raza_existente:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Raza no encontrada"
            )
        
        """# Verificar tipo de animal si se proporciona"""
        if raza_data.id_tipoAnimal:
            from Entities.Tipo_animal import Tipo_animal
            tipo_animal = db.query(Tipo_animal).filter(
                Tipo_animal.id_tipoAnimal == raza_data.id_tipoAnimal
            ).first()
            
            if not tipo_animal:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="El tipo de animal especificado no existe"
                )
        
        """# Verificar nombre único si se actualiza"""
        if raza_data.nombreRaza and raza_data.nombreRaza != raza_existente.nombreRaza:
            nombre_existente = crud.obtener_raza_por_nombre(raza_data.nombreRaza)
            if nombre_existente and nombre_existente.id_raza != raza_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Ya existe otra raza con ese nombre"
                )
        
        # Preparar datos para actualización
        campos_actualizacion = raza_data.dict(exclude_unset=True)
        
        # Actualizar raza usando el CRUD
        raza_actualizada = crud.actualizar_raza_animal(raza_id, **campos_actualizacion)
        
        if not raza_actualizada:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error al actualizar la raza"
            )
        
        return raza_actualizada
        
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al actualizar raza: {str(e)}"
        )

"""ENDPOINTS DELETE """

@router.delete("/{raza_id}", response_model=RespuestaAPI)
async def eliminar_raza(
    raza_id: UUID,
    db: Session = Depends(get_db)
):

    try:
        crud = RazaAnimalCRUD(db)
        
        # Verificar que la raza existe
        raza_existente = crud.obtener_raza(raza_id)
        if not raza_existente:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Raza no encontrada"
            )
        
        # Verificar si hay animales asociados a esta raza
        from Entities.animal import Animal
        animales_asociados = db.query(Animal).filter(
            Animal.id_raza == raza_id
        ).count()
        
        if animales_asociados > 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"No se puede eliminar la raza porque tiene {animales_asociados} animal(es) asociado(s)"
            )
        
        # Eliminar la raza usando el CRUD
        eliminado = crud.eliminar_raza_animal(raza_id)
        
        if eliminado:
            return RespuestaAPI(
                mensaje="Raza eliminada exitosamente",
                exito=True,
                datos={"id_eliminado": str(raza_id)}
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error al eliminar la raza"
            )
        
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al eliminar raza: {str(e)}"
        )

"""# ==================== ENDPOINTS ADICIONALES ===================="""

@router.get("/tipo-animal/{tipo_id}", response_model=List[RazaAnimalResponse])
async def obtener_razas_por_tipo(
    tipo_id: UUID,
    db: Session = Depends(get_db)
):

    try:
        # Verificar que el tipo existe
        from Entities.Tipo_animal import Tipo_animal
        tipo_animal = db.query(Tipo_animal).filter(
            Tipo_animal.id_tipoAnimal == tipo_id
        ).first()
        
        if not tipo_animal:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tipo de animal no encontrado"
            )
        
        crud = RazaAnimalCRUD(db)
        razas = crud.obtener_razas_por_tipo(tipo_id)
        
        return razas
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener razas por tipo: {str(e)}"
        )

@router.get("/{raza_id}/estadisticas", response_model=RespuestaAPI)
async def obtener_estadisticas_raza(
    raza_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Obtener estadísticas de animales por raza.
    
    - **raza_id**: UUID de la raza
    """
    try:
        crud = RazaAnimalCRUD(db)
        
        # Verificar que la raza existe
        raza = crud.obtener_raza(raza_id)
        if not raza:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Raza no encontrada"
            )
        
        # Contar animales por esta raza
        from Entities.animal import Animal
        total_animales = db.query(Animal).filter(Animal.id_raza == raza_id).count()
        
        # Contar por género si existe la relación
        animales_por_genero = {}
        try:
            from Entities.genero import Genero
            animales_genero = db.query(
                Animal.id_genero, 
                Genero.nombre_genero, 
                db.func.count(Animal.id_animal)
            ).join(Genero, Animal.id_genero == Genero.id_genero).filter(
                Animal.id_raza == raza_id
            ).group_by(Animal.id_genero, Genero.nombre_genero).all()
            
            animales_por_genero = {
                genero_nombre: cantidad 
                for _, genero_nombre, cantidad in animales_genero
            }
        except Exception as e:
            animales_por_genero = {"error": f"No se pudieron obtener estadísticas por género: {str(e)}"}
        
        # Obtener información del tipo de animal
        tipo_animal_nombre = raza.tipo_animal.nombre if raza.tipo_animal else "Desconocido"
        
        return RespuestaAPI(
            mensaje=f"Estadísticas para la raza {raza.nombreRaza}",
            exito=True,
            datos={
                "raza": raza.nombreRaza,
                "total_animales": total_animales,
                "animales_por_genero": animales_por_genero,
                "tipo_animal": tipo_animal_nombre
            }
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener estadísticas: {str(e)}"
        )