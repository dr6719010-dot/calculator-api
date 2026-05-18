from pydantic import BaseModel
from typing import Literal

class Numbers(BaseModel):
    operation: Literal["sum", "product", "difference", "division","log"]
    numbers: list[float]
    base: float| None = None