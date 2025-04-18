from datetime import datetime
from app.models.base import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship

class BetaFactor(Base):
    __tablename__ = "beta_factors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    value = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    step7 = relationship("Step7", back_populates="betaFactor")

    def __repr__(self):
        return f"<BetaFactor(id={self.id}, name={self.name})>"
