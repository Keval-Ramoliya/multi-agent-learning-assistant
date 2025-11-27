from sqlalchemy import Column, Integer, String, DateTime, func
from ..db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
