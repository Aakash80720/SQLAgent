from .base import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean

from sqlalchemy.orm import relationship

class Step12(Base):
    __tablename__ = "step_12"

    id = Column(Integer, primary_key=True, autoincrement=True)
    step1_id = Column(Integer, ForeignKey("step_1.id"), nullable=False)
    monitoring_signal_inspection = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    step1 = relationship("Step1", back_populates="step12")

    def __repr__(self):
        return f"<Step12(id={self.id}, step1_id={self.step1_id}, failure_mechanism_details={self.failure_mechanism_details})>"