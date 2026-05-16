from fastapi import FastAPI
from calculator import (
    calculate_sum,
    calculate_product,
    calculate_difference,
    calculate_division)

from models import Numbers

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Calculator API is live 🚀"}


@app.post("/sum")
def sum_numbers(data: Numbers):
    return {"result": calculate_sum(data.numbers)}


@app.post("/product")
def product_numbers(data: Numbers):
    return {"result": calculate_product(data.numbers)}


@app.post("/difference")
def difference_numbers(data: Numbers):
    return {"result": calculate_difference(data.numbers)}


@app.post("/division")
def division_numbers(data: Numbers):
    return {"result": calculate_division(data.numbers)}