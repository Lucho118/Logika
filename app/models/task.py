from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, func
from app.db.base import Base
import enum

class TaskStatus(str, enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    status = Column(Enum(TaskStatus), default=TaskStatus.pending, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
