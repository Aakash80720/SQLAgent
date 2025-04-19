from .base import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean

from sqlalchemy.orm import relationship

class Step6(Base):
    __tablename__ = "step_6"

    id = Column(Integer, primary_key=True, autoincrement=True)
    step1_id = Column(Integer, ForeignKey("step_1.id"), nullable=False)
    failure_and_effect = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    step5 = relationship("Step5", back_populates="step6")

    def __repr__(self):
        return f"<Step6(id={self.id}, step5_id={self.step5_id}, failure_mode_detail_id={self.failure_mode_detail_id})>"