from fastapi import FastAPI
from app.routes import employee, attendance

app = FastAPI(
    title="HRMS Lite API",
    description="Lightweight HRMS System using FastAPI + MongoDB Atlas",
    version="1.0.0"
)

app.include_router(employee.router)
app.include_router(attendance.router)
