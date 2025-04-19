from datetime import datetime
from app.models.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean

class Maintenance(Base):
    __tablename__ = "maintenances"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Maintenance(id={self.id}, name={self.name})>"