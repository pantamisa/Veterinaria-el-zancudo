"""
Módulo de operaciones CRUD
==========================

Este módulo contiene todas las operaciones CRUD (Create, Read, Update, Delete)
para las entidades del sistema.
"""

from .usuario_crud import UsuarioCRUD
from .animal_crud import AnimalCRUD
from .genero_crud import GeneroCRUD
from .Razaanimal_crud import RazaAnimalCRUD, crear_raza_animal, obtener_raza, obtener_raza_por_nombre, obtener_razas, obtener_razas_por_tipo, actualizar_raza_animal
from .Tipoanimal_crud import TipoAnimalCRUD, crear_tipo_animal, obtener_tipo_animal, obtener_tipo_por_nombre, obtener_tipos, actualizar_tipo_animal, eliminar_tipo_animal
from .citas_crud import CitaCRUD

__all__ = [
    'UsuarioCRUD', 
    'AnimalCRUD',
    'GeneroCRUD',
    'RazaAnimalCRUD',  'crear_raza_animal', 'obtener_raza', 'obtener_raza_por_nombre', 'obtener_razas', 'obtener_razas_por_tipo', 'actualizar_raza_animal',
    'TipoAnimalCRUD',  'crear_tipo_animal', 'obtener_tipo_animal', 'obtener_tipo_por_nombre', 'obtener_tipos', 'actualizar_tipo_animal', 'eliminar_tipo_animal',
    'CitaCRUD'
]