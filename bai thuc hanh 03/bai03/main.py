from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Student(BaseModel):
    id: int
    name: str
    age: int
    address: str
    phone: str
    email: str
    class_name: str

class LoginRequest(BaseModel):
    username: str
    password: str

students = [
    Student(id=1, name="Nguyen Van A", age=20, address="Ha Noi", phone="0123456789", email="a@gmail.com", class_name="CNTT1"),
    Student(id=2, name="Tran Van B", age=21, address="Hai Phong", phone="0987654321", email="b@gmail.com", class_name="CNTT2"),
    # Thêm các sinh viên khác
]

@app.post("/login")
def login(request: LoginRequest):
    if request.username == "admin" and request.password == "admin":
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Tài khoản hoặc mật khẩu không chính xác")

@app.get("/students", response_model=List[Student])
def get_students():
    return students

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
