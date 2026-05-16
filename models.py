from pydantic import BaseModel
from typing import Literal

class Numbers(BaseModel):
    operation: Literal["sum", "product", "difference", "division"]
    numbers: list[int]