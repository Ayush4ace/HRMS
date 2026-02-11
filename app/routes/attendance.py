from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from datetime import datetime
from app.database import db
from app.models.attendance import AttendanceCreate
from app.utils.responses import serialize_doc

router = APIRouter(prefix="/attendance", tags=["Attendance"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def mark_attendance(data: AttendanceCreate):

    # Validate ObjectId
    if not ObjectId.is_valid(data.employee_id):
        raise HTTPException(status_code=400, detail="Invalid employee ID")

    employee_obj_id = ObjectId(data.employee_id)

    # Check employee exists
    employee = await db.employees.find_one({"_id": employee_obj_id})
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    # Convert date → datetime (MongoDB compatible)
    attendance_date = datetime.combine(data.date, datetime.min.time())

    # Prevent duplicate attendance for same day
    existing_attendance = await db.attendance.find_one(
        {
            "employee_id": data.employee_id,
            "date": attendance_date,
        }
    )

    if existing_attendance:
        raise HTTPException(
            status_code=400,
            detail="Attendance already marked for this date",
        )

    attendance_data = {
        "employee_id": data.employee_id,
        "date": attendance_date,
        "status": data.status,
        "created_at": datetime.utcnow(),
    }

    result = await db.attendance.insert_one(attendance_data)

    new_attendance = await db.attendance.find_one(
        {"_id": result.inserted_id}
    )

    return serialize_doc(new_attendance)


@router.get("/{employee_id}")
async def get_attendance(employee_id: str):

    if not ObjectId.is_valid(employee_id):
        raise HTTPException(status_code=400, detail="Invalid employee ID")

    records = []

    async for record in db.attendance.find(
        {"employee_id": employee_id}
    ).sort("date", -1):
        records.append(serialize_doc(record))

    return records
