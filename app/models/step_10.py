from .base import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean

from sqlalchemy.orm import relationship

class Step10(Base):
    __tablename__ = "step_10"

    id = Column(Integer, primary_key=True, autoincrement=True)
    step1_id = Column(Integer, ForeignKey("step_1.id"), nullable=False)
    failure_mechanism_details = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    step1 = relationship("Step1", back_populates="step10")

    def __repr__(self):
        return f"<Step10(id={self.id}, step1_id={self.step1_id}, failure_mode_id={self.failure_mode_id})>"