from .base import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean

from sqlalchemy.orm import relationship

class Step8(Base):
    __tablename__ = "step_8"

    id = Column(Integer, primary_key=True, autoincrement=True)
    step1_id = Column(Integer, ForeignKey("step_1.id"), nullable=False)
    safety = Column(Integer,nullable=False)
    environment = Column(Integer,nullable=False)
    availability = Column(Integer,nullable=False)
    sparepart_cost = Column(Integer,nullable=False)
    intervention = Column(Integer,nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    step1 = relationship("Step1", back_populates="step8")

    def __repr__(self):
        return f"<Step8(id={self.id}, step4_id={self.step4_id}, failure_cause_details={self.failure_cause_details})>"