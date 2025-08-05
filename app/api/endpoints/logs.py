from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy import desc
from sqlalchemy.orm import Session
from ...core.database import get_db
from ...models.request_log import RequestLog
from ...schemas.common import ResultResponse

router = APIRouter()

@router.get("/logs", response_model=List[ResultResponse])
async def get_logs(limit: int = Query(50, ge=1, le=100), db: Session = Depends(get_db)):
    entries = db.query(RequestLog).order_by(desc(RequestLog.created_at)).limit(limit).all()
    return [
        ResultResponse(
            operation=e.operation,
            input=e.input_data,
            result=float(e.result) if "." in e.result else int(e.result),
            id=e.id,
            created_at=e.created_at,
        )
        for e in entries
    ]
