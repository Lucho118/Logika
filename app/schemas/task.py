from pydantic import BaseModel
from datetime import datetime
from app.models.task import TaskStatus

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    status: TaskStatus

class TaskStatusUpdate(BaseModel):
    status: TaskStatus

class TaskOut(BaseModel):
    id: int
    title: str
    description: str | None
    status: TaskStatus
    created_at: datetime

    class Config:
        from_attributes = True
