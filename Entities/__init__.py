"""
Módulo de entidades
==================

Este módulo contiene todas las entidades del sistema usando SQLAlchemy
y sus esquemas de validación con Pydantic.
"""

from .usuario import Usuario
from .animal import Animal
from .genero import Genero
from .Raza_animal import Raza_animal
from .Tipo_animal import Tipo_animal
from .Citas import Citas

__all__ = [
    # Usuario
    'Usuario',
    # Animal
    'Animal',
    # Genero
    'Genero',
    # Raza Animal
    'Raza_animal',
    # Tipo Animal
    'Tipo_animal',
    # Citas
    'Citas',
]
