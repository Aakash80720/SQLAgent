from datetime import datetime
from .base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean

from sqlalchemy.orm import relationship

class Step5(Base):
    __tablename__ = "step_5"

    id = Column(Integer, primary_key=True, autoincrement=True)
    step4_id = Column(Integer, ForeignKey("step_4.id"), nullable=False)
    failure_mode_detail_id = Column(Integer, ForeignKey("failure_mode_detail.id"), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    step1 = relationship("Step1", back_populates="step5")
    likelihood = relationship("Likelihood", back_populates="step5")

    def __repr__(self):
        return f"<Step5(id={self.id}, step4_id={self.step4_id}, failure_mode_detail_id={self.failure_mode_detail_id})>"