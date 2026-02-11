from fastapi import APIRouter, HTTPException, status
from app.database import db
from app.models.employee import EmployeeCreate
from app.utils.responses import serialize_doc

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_employee(data: EmployeeCreate):

    # Check duplicate email
    existing_email = await db.employees.find_one({"email": data.email})
    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    # Generate next employee_id
    count = await db.employees.count_documents({})
    employee_code = f"EMP{str(count + 1).zfill(3)}"

    employee_data = data.model_dump()
    employee_data["employee_id"] = employee_code

    result = await db.employees.insert_one(employee_data)
    new_employee = await db.employees.find_one({"_id": result.inserted_id})

    return serialize_doc(new_employee)


@router.get("/")
async def get_employees():
    employees = []
    async for emp in db.employees.find():
        employees.append(serialize_doc(emp))
    return employees


@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_employee(employee_id: str):

    result = await db.employees.delete_one({"_id": __import__("bson").ObjectId(employee_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
