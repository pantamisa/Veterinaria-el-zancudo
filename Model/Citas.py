from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from ..Database.config import Base
from uuid import UUID

class Citas(Base):
    """
    Modelo de Citas que representa la tabla 'Citas'
    
    Atributos:
        id_citas: Identificador único de cada cita
        id_servicio: Identificador del servicio solicitado (clave foránea)
        id_animal: Identificador del animal al que pertenece la cita (clave foránea)
        fecha_asignacion: Fecha en que se asignó la cita
        fecha_atencion: Fecha en que se atenderá la cita
    """
    
    __tablename__ = "Citas"
    
    id_citas = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    id_servicio = Column(UUID(as_uuid=True), ForeignKey("Servicios.id_servicio"), nullable=False)
    id_animal = Column(UUID(as_uuid=True), ForeignKey("Animal.id_animal"), nullable=False)
    fecha_asignacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_atencion = Column(DateTime(timezone=True), nullable=True)

    # Auditoría
    id_usuario_crea = Column(UUID(as_uuid=True), nullable=False)
    id_usuario_edita = Column(UUID(as_uuid=True), nullable=True, default=None)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

    # Relaciones
    servicio = relationship("Servicios", back_populates="citas")
    animal = relationship("Animal", back_populates="citas")
    usuario_crea = relationship("Usuario", foreign_keys=[id_usuario_crea])
    usuario_edita = relationship("Usuario", foreign_keys=[id_usuario_edita])

    def __repr__(self):
        """Representación en string del objeto Citas"""
        return f"<Cita(id={self.id_citas}, servicio='{self.id_servicio}', animal='{self.id_animal}')>"
    
    def to_dict(self):
        """Convierte el objeto a un diccionario"""
        return {
            "id_citas": self.id_citas,
            "id_servicio": self.id_servicio,
            "id_animal": self.id_animal,
            "fecha_asignacion": self.fecha_asignacion,
            "fecha_atencion": self.fecha_atencion
        }
