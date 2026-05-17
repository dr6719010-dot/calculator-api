from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from calculator import (
    calculate_sum,
    calculate_product,
    calculate_difference,
    calculate_division
)
from models import Numbers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

operations = {
    "sum": calculate_sum,
    "product": calculate_product,
    "difference": calculate_difference,
    "division": calculate_division
}

@app.get("/")
def home():
    return {"message": "Calculator API is live 🚀"}

@app.get("/history")
def get_history():
    return {
        "history": [
            {"operation": "sum", "result": 60},
            {"operation": "product", "result": 24},
            {"operation": "difference", "result": -4}
        ]
    }

@app.post("/calculate")
def calculate(data: Numbers):
    operation = operations[data.operation]
    result = operation(data.numbers)
    return {"operation": data.operation, "result": result}