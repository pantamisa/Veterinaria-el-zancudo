"""
Módulo de entidades
==================

Este módulo contiene todas las entidades del sistema usando SQLAlchemy
y sus esquemas de validación con Pydantic.
"""

from .usuario import Usuario, UsuarioCreate, UsuarioUpdate, UsuarioResponse
from .animal import Animal, AnimalCreate, AnimalUpdate, AnimalResponse
from .genero import Genero, GeneroCreate, GeneroResponse
from .Raza_animal import RazaAnimal, RazaAnimalCreate, RazaAnimalUpdate, RazaAnimalResponse
from .Tipo_animal import TipoAnimal, TipoAnimalCreate, TipoAnimalUpdate, TipoAnimalResponse
from .Citas import Cita, CitaCreate, CitaUpdate, CitaResponse

__all__ = [
    # Usuario
    'Usuario', 'UsuarioCreate', 'UsuarioUpdate', 'UsuarioResponse',
    # Animal
    'Animal', 'AnimalCreate', 'AnimalUpdate', 'AnimalResponse',
    # Genero
    'Genero', 'GeneroCreate', 'GeneroResponse',
    # Raza Animal
    'RazaAnimal', 'RazaAnimalCreate', 'RazaAnimalUpdate', 'RazaAnimalResponse',
    # Tipo Animal
    'TipoAnimal', 'TipoAnimalCreate', 'TipoAnimalUpdate', 'TipoAnimalResponse',
    # Citas
    'Cita', 'CitaCreate', 'CitaUpdate', 'CitaResponse',
]
