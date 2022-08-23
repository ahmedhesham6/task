from sqlalchemy.sql.expression import true
from . import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Balance, BalanceEvent, BalanceEventTypeEnum
from schema import BalanceEventBase
from services import BalanceEventService

router = APIRouter(
    tags=["balance"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def find(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    balances = db.query(Balance).offset(skip).limit(limit).all()
    return {"message": "Balances Fetched Successfully", "data": balances}


@router.post("/deposit")
def deposit(balance_event: BalanceEventBase, db: Session = Depends(get_db)):
    BalanceEventService.deposit(
        user_id=balance_event.user_id, amount=balance_event.amount, db=db)
    db.commit()
    return {"message": "Amount is deposited successfully"}


@router.post("/withdraw")
def withdraw(balance_event: BalanceEventBase, db: Session = Depends(get_db)):
    try:
        BalanceEventService.withdraw(
            user_id=balance_event.user_id, amount=balance_event.amount, db=db)
        db.commit()
        return {"message": "Amount withdrawn successfully"}
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
