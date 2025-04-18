from .base import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean

from sqlalchemy.orm import relationship

class Step7(Base):
    __tablename__ = "step_7"

    id = Column(Integer, primary_key=True, autoincrement=True)
    step1_id = Column(Integer, ForeignKey("step_1.id"), nullable=False)
    beta_factor = Column(Integer,ForeignKey("beta_factors.id"), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    step1 = relationship("Step1", back_populates="step7")
    betaFactor = relationship("BetaFactor", back_populates="step7")

    def __repr__(self):
        return f"<Step7(id={self.id}, step1_id={self.step1_id}, failure_cause_details={self.failure_cause_details})>"