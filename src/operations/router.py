import time

from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from operations.models import operation
from operations.schemas import OperationCreate

router = APIRouter(
    prefix="/operations",
    tags=["Operation"],
)


@router.get("/long_operation")
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return "There is some data before we send it to front"


@router.get("/")
async def get_specific_operations(
    operation_type: str, session: AsyncSession = Depends(get_async_session)
):
    try:
        query = select(operation).where(operation.c.type == operation_type)
        result = await session.execute(query)
        result_dict = result.mappings().all()
    except Exception:
        raise HTTPException(
            status_code=500,
            detail={"status": "error", "data": None, "details": None},
        )
    return {
        "status": "success",
        "data": result_dict,
        "details": None,
    }


@router.post("/")
async def add_specific_operation(
    new_operation: OperationCreate,
    session: AsyncSession = Depends(get_async_session),
):
    stmt = insert(operation).values(**new_operation.model_dump())
    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}
