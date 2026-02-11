from fastapi import FastAPI
from app.routes import employee, attendance
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost:5173",
    "http://localhost:127.0.0.1:5173",
    "https://hrms-frontend-xi-one.vercel.app/"
]

app = FastAPI(
    title="HRMS Lite API",
    description="Lightweight HRMS System using FastAPI + MongoDB Atlas",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employee.router)
app.include_router(attendance.router)


@app.get("/")
def root():
    return {"message": "HRMS API is running 🚀"}
