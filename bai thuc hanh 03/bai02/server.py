from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
print("FastAPI imported successfully")
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["null", "*", "http://localhost:3000", "http://localhost:8001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CalculationRequest(BaseModel):
    a: float
    b: float

@app.post("/add")
def add(request: CalculationRequest):
    return {"result": request.a + request.b}

@app.post("/subtract")
def subtract(request: CalculationRequest):
    return {"result": request.a - request.b}

@app.post("/multiply")
def multiply(request: CalculationRequest):
    return {"result": request.a * request.b}

@app.post("/divide")
def divide(request: CalculationRequest):
    if request.b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result": request.a / request.b}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
