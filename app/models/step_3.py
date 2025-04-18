from .base import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean

from sqlalchemy.orm import relationship

class Step3(Base):
    __tablename__ = "step_3"

    id = Column(Integer, primary_key=True, autoincrement=True)
    step1_id = Column(Integer, ForeignKey("step_1.id"), nullable=False)
    failure_mode_id = Column(Integer, ForeignKey("failure_modes.id"), nullable=False)
    failure_mode_details_id = Column(Integer, ForeignKey("failure_mode_detail.id"), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    step1 = relationship("Step1", back_populates="step3")
    failure_mode = relationship("FailureMode", back_populates="step3")
    failure_mode_details = relationship("FailureModeDetails", back_populates="step3")

    def __repr__(self):
        return f"<Step3(id={self.id}, step2_id={self.step2_id}, failure_mode_id={self.failure_mode_id})>"