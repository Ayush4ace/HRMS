HRMS BACKEND 

TECH STACK 

1. FAST API
2. MONGODB 
3. PYDANTIC
4. UV(python package manager)


Features 

1. CREATE EMPLOYEE 
2. LIST EMPLOYEE 
3. DELETE EMPLOYEE
4. MARK ATTENDANCE 
5. DUPLICATE ATTENDANCE PREVENTION 
6. ASYNC DATABASE OPERATION
7. AUTO GENERATED SWAGGER DOCS 

for seeing API's go to ${BASE_URL}/docs






ENVIORNMENT SETUP 

uv venv 
source .venv/bin/activate


INSTALL DEPENDENCIES 

uv add fastapi uvicorn motor python-dotenv pydantic-settings


and create a .env file in the root folder 

and put these variable 

MONGO_URL=
DATABASE_NAME=


RUN SERVER 

uv run uvicorn app.main:app --reload


server runs at http://127.0.0.1:8000


API DOCUMENTAION

http://127.0.0.1:8000/docs

