# FastAPI Student Management Project

Welcome to the FastAPI Student Management Project! This project demonstrates the use of FastAPI, a modern web framework for building APIs with Python, to create a simple student management system.

## Features

- **CRUD Operations**: Perform Create, Read, Update, and Delete operations on student records.
- **HTTP Endpoints**: Easily interact with the system via HTTP endpoints.
- **In-Memory Storage**: Utilizes a Python dictionary for storing student data.
- **Basic Python**: Demonstrates basic Python programming without Pydantic type enforcement.

## Usage

1. **Clone the Repository**: `git clone https://github.com/motunmarteen/FastAPI-Student-Management-Project.git`
2. **Navigate to the Project Directory**: `cd FastAPI-Student-Management-Project`
3. **Install Dependencies**: `pip install -r requirements.txt`
4. **Run the FastAPI Server**: `uvicorn main:app --reload`
5. **Access API Documentation**: Open http://localhost:8000/docs in your browser to view interactive API documentation.

## Endpoints

- **POST /students**: Create a new student record.
- **GET /students/{student_id}**: Retrieve a specific student record by ID.
- **GET /students**: Retrieve all student records.
- **PUT /students/{student_id}**: Update an existing student record by ID.
- **DELETE /students/{student_id}**: Delete a student record by ID.

## Contributions

Contributions and feedback are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request.
