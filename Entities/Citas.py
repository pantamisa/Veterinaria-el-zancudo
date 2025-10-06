from sqlalchemy import Column, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from Database.config import Base
import uuid

class Citas(Base):
    __tablename__ = "citas"

    id_citas = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    id_servicio = Column(UUID(as_uuid=True), ForeignKey("servicios.id_servicio"), nullable=False)
    id_animal = Column(UUID(as_uuid=True), ForeignKey("animales.id_animal"), nullable=False)
    
    fecha_asignacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_atencion = Column(DateTime(timezone=True), nullable=True)

    # Relaciones
    servicio = relationship("Servicios", back_populates="citas")
    animal = relationship("Animal", back_populates="citas")
    facturas = relationship("Factura", back_populates="cita", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Cita(id={self.id_citas}, servicio='{self.id_servicio}', animal='{self.id_animal}')>"

    def to_dict(self):
        return {
            "id_citas": self.id_citas,
            "id_servicio": self.id_servicio,
            "id_animal": self.id_animal,
            "fecha_asignacion": self.fecha_asignacion,
            "fecha_atencion": self.fecha_atencion
        }
