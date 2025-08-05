from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...core.database import get_db
from ...models.request_log import RequestLog
from ...services.math_ops import fib_op, factorial_op, pow_op, sqrt_op
from ...schemas.common import PowRequest, ResultResponse

router = APIRouter()

@router.post("/pow", response_model=ResultResponse)
async def power(payload: PowRequest, db: Session = Depends(get_db)):
    result = pow_op(payload.base, payload.exponent)
    entry = RequestLog(operation="pow", input_data=payload.dict(), result=str(result))
    db.add(entry); db.flush()
    return ResultResponse(operation="pow", input=payload.dict(), result=result, id=entry.id, created_at=entry.created_at)

@router.get("/fib/{n}", response_model=ResultResponse)
async def fibonacci(n: int, db: Session = Depends(get_db)):
    result = fib_op(n)
    entry = RequestLog(operation="fib", input_data=n, result=str(result))
    db.add(entry); db.flush()
    return ResultResponse(operation="fib", input=n, result=result, id=entry.id, created_at=entry.created_at)

@router.get("/factorial/{n}", response_model=ResultResponse)
async def factorial(n: int, db: Session = Depends(get_db)):
    result = factorial_op(n)
    entry = RequestLog(operation="factorial", input_data=n, result=str(result))
    db.add(entry); db.flush()
    return ResultResponse(operation="factorial", input=n, result=result, id=entry.id, created_at=entry.created_at)

@router.get("/sqrt/{x}", response_model=ResultResponse)
async def sqrt(x: float, db: Session = Depends(get_db)):
    result = sqrt_op(x)
    entry = RequestLog(operation="sqrt", input_data=x, result=str(result))
    db.add(entry); db.flush()
    return ResultResponse(operation="sqrt", input=x, result=result, id=entry.id, created_at=entry.created_at)
