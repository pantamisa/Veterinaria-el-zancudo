from sqlalchemy import Column, String, DateTime, ForeignKey, Float, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from Database.config import Base
import uuid

class Servicios(Base):
    # ✅ CORREGIDO: tabla en minúscula por convención
    __tablename__ = "servicios"  # Cambié de "Servicios" a "servicios"
    
    id_servicio = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    nombre_ser = Column(String(100), nullable=False, unique=True)
    costo = Column(Float, nullable=False)
    
    # Relación con citas
    citas = relationship("Citas", back_populates="servicio", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Servicio(id={self.id_servicio}, nombre='{self.nombre_ser}', costo={self.costo})>"
    
    def to_dict(self):
        return {
            "id_servicio": self.id_servicio,
            "nombre_ser": self.nombre_ser,
            "costo": self.costo
        }