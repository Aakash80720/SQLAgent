from app.models.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean

from sqlalchemy.orm import relationship
from datetime import datetime

class FailureModeDetails(Base):
    __tablename__ = "failure_mode_detail"

    id = Column(Integer, primary_key=True, autoincrement=True)
    failure_mode_id = Column(Integer, ForeignKey("failure_modes.id"), nullable=False)
    description = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    failure_mode = relationship("FailureMode", back_populates="failure_mode_details")
    step3 = relationship("Step3", back_populates="failure_mode_details")

    def __repr__(self):
        return f"<FailureModeDetails(id={self.id}, failure_mode_id={self.failure_mode_id}, description={self.description})>"
    
