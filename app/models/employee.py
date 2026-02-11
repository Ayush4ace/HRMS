from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from bson import ObjectId

class EmployeeCreate(BaseModel):
    
    full_name: str = Field(..., min_length=1)
    email: EmailStr
    department: str = Field(..., min_length=1)

class EmployeeResponse(EmployeeCreate):
    id: str
