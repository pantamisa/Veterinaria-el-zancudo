from sqlalchemy import Column, String, DateTime, ForeignKey, Float, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID   # 👈 este es el correcto
from Database.config import Base
import uuid  # 👈 para generar nuevos UUIDs

class Servicios(Base):
    """
    Modelo de Servicios que representa la tabla 'Servicios'
    
    Atributos:
        id_servicio: Identificador único del servicio
        nombre_ser: Nombre del servicio (ejemplo: vacunación, lavado, etc.)
        costo: Costo del servicio
    """
    
    __tablename__ = "Servicios"
    
    id_servicio = Column(
        UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid.uuid4,        # 👈 genera automáticamente un UUID nuevo
        nullable=False
    )
    nombre_ser = Column(String(100), nullable=False, unique=True)
    costo = Column(Float, nullable=False)

    # Auditoría
    id_usuario_crea = Column(UUID(as_uuid=True), nullable=False)
    id_usuario_edita = Column(UUID(as_uuid=True), nullable=True, default=None)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())

    # Relaciones
    citas = relationship("Citas", back_populates="servicio")

    usuario_crea = relationship("Usuario", foreign_keys=[id_usuario_crea])
    usuario_edita = relationship("Usuario", foreign_keys=[id_usuario_edita])

    def __repr__(self):
        """Representación en string del objeto Servicios"""
        return f"<Servicio(id={self.id_servicio}, nombre='{self.nombre_ser}', costo={self.costo})>"
    
    def to_dict(self):
        """Convierte el objeto a un diccionario"""
        return {
            "id_servicio": self.id_servicio,
            "nombre_ser": self.nombre_ser,
            "costo": self.costo
        }
