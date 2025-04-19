import datetime
from app.models.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship

class FailureMode(Base):
    __tablename__ = "failure_modes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.UTC)
    updated_at = Column(DateTime, default=datetime.UTC, onupdate=datetime.UTC)

    failure_mode_details = relationship("FailureModeDetails", back_populates="failure_mode")
    step3 = relationship("Step3", back_populates="failure_mode")

    def __repr__(self):
        return f"<FailureMode(id={self.id}, name={self.name})>"
    

