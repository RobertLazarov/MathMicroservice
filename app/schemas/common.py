from datetime import datetime
from typing import Union
from pydantic import BaseModel, Field

class PowRequest(BaseModel):
    base: float = Field(..., description="Base value")
    exponent: float = Field(..., description="Exponent value")

class ResultResponse(BaseModel):
    operation: str
    input: Union[dict, int, float]
    result: Union[int, float]
    id: int
    created_at: datetime
