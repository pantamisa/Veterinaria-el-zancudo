"""
Módulo de operaciones CRUD
==========================

Este módulo contiene todas las operaciones CRUD (Create, Read, Update, Delete)
para las entidades del sistema.
"""

from .usuario_crud import UsuarioCRUD
from .animal_crud import AnimalCRUD
from .genero_crud import GeneroCRUD
from .raza_animal_crud import RazaAnimalCRUD
from .tipo_animal_crud import TipoAnimalCRUD
from .citas_crud import CitaCRUD

__all__ = [
    'UsuarioCRUD',
    'AnimalCRUD',
    'GeneroCRUD',
    'RazaAnimalCRUD',
    'TipoAnimalCRUD',
    'CitaCRUD'
]