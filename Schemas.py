"""
Schemas Pydantic para el Sistema de Gestión Veterinaria El Zancudo
"""

from datetime import datetime
from typing import Optional, List
from uuid import UUID
from decimal import Decimal
from pydantic import BaseModel, EmailStr, Field, validator


"""schemas del los Usuraios"""
class UsuarioBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    apellido: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    telefono: Optional[str] = Field(None, max_length=20)
    es_admin: bool = False


class UsuarioCreate(UsuarioBase):
    password: str = Field(..., min_length=6)


class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = Field(None, max_length=100)
    apellido: Optional[str] = Field(None, max_length=100)
    email: Optional[EmailStr] = None
    telefono: Optional[str] = Field(None, max_length=20)
    es_admin: Optional[bool] = None
    password: Optional[str] = Field(None, min_length=6)


class UsuarioResponse(UsuarioBase):
    id_usuario: UUID

    class Config:
        from_attributes = True


class UsuarioLogin(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    token: str
    usuario: UsuarioResponse


class CambioContraseña(BaseModel):
    contraseña_actual: str
    nueva_contraseña: str = Field(..., min_length=6)


"""schemas del los generos"""
class GeneroBase(BaseModel):
    nombre_genero: str = Field(..., min_length=1, max_length=10)

    @validator('nombre_genero')
    def validar_nombre(cls, v):
        if not v.strip():
            raise ValueError('El nombre del género no puede estar vacío')
        return v.strip()


class GeneroCreate(GeneroBase):
    pass


class GeneroUpdate(BaseModel):
    nombre_genero: Optional[str] = Field(None, max_length=10)


class GeneroResponse(GeneroBase):
    id_genero: UUID

    class Config:
        from_attributes = True


"""schemas del los tipos de animal"""
class TipoAnimalBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)


class TipoAnimalCreate(TipoAnimalBase):
    pass


class TipoAnimalUpdate(BaseModel):
    nombre: Optional[str] = Field(None, max_length=100)


class TipoAnimalResponse(TipoAnimalBase):
    id_tipoAnimal: UUID

    class Config:
        from_attributes = True



"""schemas del los tipos de raza animal"""
class RazaAnimalBase(BaseModel):
    nombreRaza: str = Field(..., min_length=1, max_length=100)
    id_tipoAnimal: UUID


class RazaAnimalCreate(RazaAnimalBase):
    pass


class RazaAnimalUpdate(BaseModel):
    nombreRaza: Optional[str] = Field(None, max_length=100)
    id_tipoAnimal: Optional[UUID] = None


class RazaAnimalResponse(RazaAnimalBase):
    id_raza: UUID

    class Config:
        from_attributes = True


class RazaAnimalConTipo(RazaAnimalResponse):
    tipo_animal: TipoAnimalResponse



"""schemas del los animales"""
class AnimalBase(BaseModel):
    nombre_animal: str = Field(..., min_length=1, max_length=200)
    edad_animal: str = Field(..., max_length=4)
    id_genero: UUID
    id_raza: UUID


class AnimalCreate(AnimalBase):
    id_usuario: UUID  # propietario
    id_usuario_crea: UUID  # quien lo registra


class AnimalUpdate(BaseModel):
    nombre_animal: Optional[str] = Field(None, max_length=200)
    edad_animal: Optional[str] = Field(None, max_length=4)
    id_genero: Optional[UUID] = None
    id_raza: Optional[UUID] = None
    id_usuario_edita: Optional[UUID] = None


class AnimalResponse(AnimalBase):
    id_animal: UUID
    id_usuario: UUID
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None

    class Config:
        from_attributes = True


class AnimalConRelaciones(AnimalResponse):
    genero: GeneroResponse
    raza: RazaAnimalConTipo
    usuario_propietario: UsuarioResponse


"""schemas del los servicios"""
class ServicioBase(BaseModel):
    nombre_ser: str = Field(..., min_length=1, max_length=100)
    costo: float = Field(..., gt=0)

    @validator('costo')
    def validar_costo(cls, v):
        if v <= 0:
            raise ValueError('El costo debe ser mayor a 0')
        return v


class ServicioCreate(ServicioBase):
    pass


class ServicioUpdate(BaseModel):
    nombre_ser: Optional[str] = Field(None, max_length=100)
    costo: Optional[float] = Field(None, gt=0)


class ServicioResponse(ServicioBase):
    id_servicio: UUID

    class Config:
        from_attributes = True


"""schemas del las citas"""
class CitaBase(BaseModel):
    id_servicio: UUID
    id_animal: UUID
    fecha_atencion: Optional[datetime] = None


class CitaCreate(CitaBase):
    id_usuario_crea: UUID


class CitaUpdate(BaseModel):
    id_servicio: Optional[UUID] = None
    id_animal: Optional[UUID] = None
    fecha_atencion: Optional[datetime] = None
    id_usuario_edita: Optional[UUID] = None


class CitaResponse(CitaBase):
    id_citas: UUID
    fecha_asignacion: datetime

    class Config:
        from_attributes = True


class CitaConRelaciones(CitaResponse):
    servicio: ServicioResponse
    animal: AnimalConRelaciones
    usuario_crea: UsuarioResponse


class CitaDetallada(CitaResponse):
    servicio: ServicioResponse
    animal: AnimalResponse
    costo_servicio: float



"""schemas del las facturas"""
class FacturaBase(BaseModel):
    id_cita: UUID
    costo: Decimal = Field(..., gt=0, decimal_places=2)
    id_usuario_pago: UUID


class FacturaCreate(FacturaBase):
    pass


class FacturaUpdate(BaseModel):
    costo: Optional[Decimal] = Field(None, gt=0, decimal_places=2)
    pagada: Optional[bool] = None
    fecha_pago: Optional[datetime] = None


class FacturaResponse(FacturaBase):
    id_factura: UUID
    fecha_generacion: datetime
    fecha_pago: Optional[datetime] = None
    pagada: bool

    class Config:
        from_attributes = True


class FacturaConRelaciones(FacturaResponse):
    cita: CitaConRelaciones
    usuario_pago: UsuarioResponse


class FacturaDetallada(FacturaResponse):
    cita: CitaDetallada
    usuario_pago: UsuarioResponse
    animal_nombre: str
    servicio_nombre: str

"""las respuestas de la api"""
class RespuestaAPI(BaseModel):
    mensaje: str
    exito: bool = True
    datos: Optional[dict] = None


class RespuestaError(BaseModel):
    mensaje: str
    exito: bool = False
    error: str
    codigo: int


class RespuestaLista(BaseModel):
    mensaje: str
    exito: bool = True
    total: int
    datos: List[dict]


class ServicioConUsoResponse(BaseModel):
    """Schema para servicio con cantidad de usos"""
    id_servicio: str
    nombre_servicio: str
    costo: float
    total_citas: int

    class Config:
        from_attributes = True

class ServicioConUsoResponseRaza(BaseModel):
    """Schema para servicio con cantidad de usos"""
    id_raza: str
    nombre_raza: str
    tipo_animal: str
    total_animales: int
    
    class Config:
        from_attributes = True
