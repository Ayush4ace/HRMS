from pydantic import BaseModel
from datetime import date
from enum import Enum


class AttendanceStatus(str, Enum):
    Present = "Present"
    Absent = "Absent"
    Leave = "Leave"


class AttendanceCreate(BaseModel):
    employee_id: str
    date: date
    status: AttendanceStatus
