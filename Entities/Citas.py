
import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from Database.config import Base


class Citas(Base):
    """
    Modelo de Citas que representa las citas asignadas a animales/servicios
    """
    __tablename__ = "citas"   # 👈 minúscula por convención

    id_citas = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)

    # FK
    id_servicio = Column(UUID(as_uuid=True), ForeignKey("servicios.id_servicio"), nullable=False)
    id_animal = Column(UUID(as_uuid=True), ForeignKey("animales.id_animal"), nullable=False)

    fecha_asignacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_atencion = Column(DateTime(timezone=True), nullable=True)

    id_usuario_crea = Column(UUID(as_uuid=True), ForeignKey("usuarios.id_usuario"), nullable=False)
    id_usuario_edita = Column(UUID(as_uuid=True), ForeignKey("usuarios.id_usuario"), nullable=True)

    # 🔹 Relaciones
    servicio = relationship("Servicios", back_populates="citas")
    animal = relationship("Animal", back_populates="citas")
    usuario_crea = relationship("Usuario", foreign_keys=[id_usuario_crea])
    usuario_edita = relationship("Usuario", foreign_keys=[id_usuario_edita])
    
    # Si tienes Factura y la relación va de Factura -> Citas:
    facturas = relationship("Factura", back_populates="cita", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Citas(id_citas={self.id_citas}, servicio='{self.id_servicio}', animal='{self.id_animal}')>"


    def to_dict(self):
        return {
            "id_citas": self.id_citas,
            "id_servicio": self.id_servicio,
            "id_animal": self.id_animal,
            "fecha_asignacion": self.fecha_asignacion,
            "fecha_atencion": self.fecha_atencion
        }
