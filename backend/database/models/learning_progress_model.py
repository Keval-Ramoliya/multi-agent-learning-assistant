# backend/database/models/learning_progress_model.py
from sqlalchemy import Column, Integer, String, DateTime, Enum, func, Text
from ..db import Base

class LearningProgress(Base):
    __tablename__ = "learning_progress"
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(64), index=True, nullable=False)
    topic = Column(String(200), nullable=False)
    level = Column(String(32), nullable=True)   # beginner/intermediate/advanced
    last_score = Column(Integer, nullable=True)
    notes = Column(Text, nullable=True)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
