from pydantic import BaseModel

class ScheduleEvent(BaseModel):
    name: str
    date: int
    time: str

class ScheduleResponse(BaseModel):
    schedule: list[ScheduleEvent]
    droppedGoals: list[str]
