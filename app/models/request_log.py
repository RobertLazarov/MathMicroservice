from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, JSON, String
from ..core.database import Base

class RequestLog(Base):
    __tablename__ = "request_logs"
    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String, index=True)
    input_data = Column(JSON)
    result = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
