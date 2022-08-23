from . import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Order, balance
from schema import OrderBase
from services import OrderService, StockService, BalanceService, BalanceEventService

router = APIRouter(
    tags=["orders"],
    responses={404: {"description": "Not found"}},
)


@router.post("/buy")
def buy(order: OrderBase, db: Session = Depends(get_db)):
    try:
        stock = StockService.find_by_id(stock_id=order.stock_id, db=db)
        OrderService.validate_buy_order(stock=stock, order=order)
        BalanceEventService.withdraw(
            user_id=order.user_id, amount=order.total * stock.price, db=db)
        OrderService.buy(order={
            "user_id": order.user_id,
            "stock_id": order.stock_id,
            "amount": order.total,
            "unit_price": stock.price,
        }, db=db)
        db.commit()
        return {"message": "Buy order has been executed successfully"}
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))


@router.post("/sell")
def sell(order: OrderBase, db: Session = Depends(get_db)):
    try:
        stock = StockService.find_by_id(stock_id=order.stock_id, db=db)
        OrderService.validate_sell_order(stock=stock, order=order)
        BalanceEventService.deposit(
            user_id=order.user_id, amount=order.total * stock.price, db=db)
        OrderService.sell(order={
            "user_id": order.user_id,
            "stock_id": order.stock_id,
            "amount": order.amount,
            "unit_price": stock.price,
        }, db=db)
        db.commit()
        return {"message": "Sell order has been executed successfully"}
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
