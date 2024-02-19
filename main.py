from fastapi import FastAPI, Response, status, HTTPException
from random import randrange
from typing import Optional

app = FastAPI()

# Dictionary to store student records, keyed by student ID
students = {
    1868644567890: {"name": "Ifunaya Johnson", "age": 18, "sex": "female", "height": 1.63},
    1345678765439: {"name": "Adewale Ayuba", "age": 17, "sex": "male", "height": 1.52},
    1997654345678: {"name": "Muhammad Salisu", "age": 19, "sex": "male", "height": 1.60},
    4132456785579: {"name": "Duke Paul", "age": 16, "sex": "male", "height": 1.4},
    1663697456890: {"name": "Faizah Timilehin", "age": 18, "sex": "female", "height": 1.67}
}

# Function to find a student by ID
def find_student(id):
    return students.get(id)

# Function to update a student record by ID
def update_student(id, name=None, age=None, sex=None, height=None):
    student = students.get(id)
    if student is None:
        return None
    if name is not None:
        student["name"] = name
    if age is not None:
        student["age"] = age
    if sex is not None:
        student["sex"] = sex
    if height is not None:
        student["height"] = height
    return student

# Function to delete a student record by ID
def delete_student(id):
    return students.pop(id, None)


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Student Management System"}


@app.get("/students")
def get_students():
    return {"data": students}


@app.post("/students", status_code=status.HTTP_201_CREATED)
def create_students(name: str, age: int, sex: str, height: float):
    id = randrange(0, 9247469240284028)
    student = {
        "name": name,
        "age": age,
        "sex": sex,
        "height": height
    }
    students[id] = student
    return {"message": "A new student is created successfully with the following student data", "data": student}


@app.get("/students/{id}")
def get_student(id: int):
    student = find_student(id)
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with id {id} does not exist")
    return {"student details": student}


@app.put("/students/{id}")
def put_student(id: int, name: Optional[str] = None, age: Optional[int] = None, sex: Optional[str] = None, height: Optional[float] = None):
    student = update_student(id, name, age, sex, height)
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with id {id} does not exist")
    return {"message": "Student details updated successfully", "data": student}


@app.delete("/students/{id}")
def delete_student_endpoint(id: int):
    if delete_student(id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with id {id} does not exist")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
