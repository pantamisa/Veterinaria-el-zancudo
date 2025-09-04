"""
Módulo de entidades
==================

Este módulo contiene todas las entidades del sistema usando SQLAlchemy
y sus esquemas de validación con Pydantic.
"""

from .usuario import Usuario, UsuarioCreate, UsuarioUpdate, UsuarioResponse

__all__ = [
    # Usuario
    'Usuario', 'UsuarioCreate', 'UsuarioUpdate', 'UsuarioResponse',
]
