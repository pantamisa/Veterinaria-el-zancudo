import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, Boolean, ForeignKey, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from Database.config import Base

class Factura(Base):
    __tablename__ = "facturas"

    # PK
    id_factura = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)

    # Fechas
    fecha_generacion = Column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    fecha_pago = Column(DateTime(timezone=True), nullable=True)

    # Estado de pago
    pagada = Column(Boolean, default=False, nullable=False)

    # FK a cita - ✅ CORREGIDO: tabla en minúscula
    id_cita = Column(UUID(as_uuid=True), ForeignKey("citas.id_citas"), nullable=False)

    # Costo del servicio
    costo = Column(Numeric(10, 2), nullable=False)

    # FK usuario que paga
    id_usuario_pago = Column(UUID(as_uuid=True), ForeignKey("usuarios.id_usuario"), nullable=True)

    # ✅ RELACIONES CORREGIDAS
    cita = relationship("Citas", back_populates="facturas")  # Singular y back_populates correcto
    usuario_pago = relationship("Usuario")  # Sin back_populates porque Usuario no lo define

    def __repr__(self):
        return (
            f"<Factura(id_factura={self.id_factura}, pagada={self.pagada}, "
            f"costo={self.costo}, id_cita={self.id_cita}, id_usuario_pago={self.id_usuario_pago})>"
        )

    def to_dict(self):
        return {
            "id_factura": str(self.id_factura),
            "fecha_generacion": self.fecha_generacion.isoformat() if self.fecha_generacion else None,
            "fecha_pago": self.fecha_pago.isoformat() if self.fecha_pago else None,
            "pagada": self.pagada,
            "id_cita": str(self.id_cita),
            "costo": float(self.costo) if self.costo is not None else None,
            "id_usuario_pago": str(self.id_usuario_pago),
        }
