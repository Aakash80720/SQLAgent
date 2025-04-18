from .base import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship

class Step1(Base):
    __tablename__ = "step_1"

    id = Column(Integer, primary_key=True, autoincrement=True)
    subsystem_component = Column(String(255), nullable=False)
    subsystem_l1 = Column(String(255), nullable=True)
    subsystem_l2 = Column(String(255), nullable=True)
    subsystem_l3 = Column(String(255), nullable=True)
    subsystem_l4 = Column(String(255), nullable=True)
    subsystem_l5 = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    step2 = relationship("Step2", back_populates="step1")
    step3 = relationship("Step3", back_populates="step1")
    step4 = relationship("Step4", back_populates="step1")
    step5 = relationship("Step5", back_populates="step1")
    step6 = relationship("Step6", back_populates="step1")
    step7 = relationship("Step7", back_populates="step1")
    step8 = relationship("Step8", back_populates="step1")
    step9 = relationship("Step9", back_populates="step1")
    step10 = relationship("Step10", back_populates="step1")
    step11 = relationship("Step11", back_populates="step1")
    step12 = relationship("Step12", back_populates="step1")
    step13 = relationship("Step13", back_populates="step1")
    step14 = relationship("Step14", back_populates="step1")

    def __repr__(self):
        return f"<Step1(id={self.id}, name={self.name})>"