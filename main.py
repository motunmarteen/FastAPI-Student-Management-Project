from fastapi import FastAPI, Response, status, HTTPException
from random import randrange
from typing import Optional

app = FastAPI()

students = [
    {"name": "Ifunaya Johnson", "age": 18, "sex": "female", "height": 1.63, "id": 10},
    {"name": "Adewale Ayuba", "age": 17, "sex": "male", "height": 1.52, "id": 13},
    {"name": "Muhammad Salisu", "age": 19, "sex": "male", "height": 1.60, "id": 19},
    {"name": "Duke Paul", "age": 16, "sex": "male", "height": 1.4, "id": 45},
    {"name": "Faizah Timilehin", "age": 18, "sex": "female", "height": 1.67, "id": 1}
    ]




def find_student(id):
    for one_student in students:
        if one_student["id"] == id:
            return one_student
        
        
        
        
def find_index_student(id):
    for i, p in enumerate(students):
        if p["id"] == id:
            return i




# GET /**: Retrieve students welcome page.
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Student Management System"}



# GET /students**: Retrieve all student records.
@app.get("/students")
def get_posts():
    return {"data": students}



# POST /students** : Create a new student record.
@app.post("/students", status_code=status.HTTP_201_CREATED)
def create_students(name: str, age: int, sex: str, height: float):
    id = randrange(0, 9247469240284028)
    student = {
        "name": name,
        "age": age,
        "sex": sex,
        "height": height,
        "id": id
    }
    students.append(student)
    return {"message": "A new student is created successfully with the following student data", "data": student}



# GET /students/{student_id}**: Retrieve a specific student record by ID.
@app.get("/students/{id}")
def get_student(id: int):
    student = find_student(id)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with id {id} does not exist")
    return {"student details": student}    



# PUT /students/{id}**: Update an existing student record by ID.
@app.put("/students/{id}")
def update_student(id: int, name: Optional[str] = None, age: Optional[int] = None, sex: Optional[str] = None, height: Optional[float] = None):
    student = find_student(id)
    
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with id {id} does not exist")
    
    if name is not None:
        student["name"] = name
    if age is not None:
        student["age"] = age
    if sex is not None:
        student["sex"] = sex
    if height is not None:
        student["height"] = height
    
    return {"message": "Student details updated successfully", "data": student}



# DELETE /students/{id}**: Delete a student record by ID.
@app.delete("/students/{id}")
def delete_student(id: int):
    index = find_index_student(id)
    
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"student with id {id} does not exist.")
    
    students.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)