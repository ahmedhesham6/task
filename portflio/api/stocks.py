from . import get_db
from uuid import UUID
from sqlalchemy.sql.expression import true
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from models import Stock
from services import StockService


router = APIRouter(
    tags=["stocks"],
    responses={404: {"description": "Not found"}},
)


@router.post("/stock")
def stock(stock_id: UUID, db: Session = Depends(get_db)):
    try:
        stock = StockService.find_by_id(stock_id=stock_id, db=db)
        return {"message": "Fetched stock", "data": stock}
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
