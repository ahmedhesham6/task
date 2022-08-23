from uuid import UUID
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from models import Stock, Order, OrderTypeEnum
from schema import OrderCreate, OrderBase


class OrderService:

    def price_within_bound(price: float, lower_bound: float, upper_bound: float):
        if (price < lower_bound or price > upper_bound):
            raise ValueError('Price is not within bound')
        return True

    def check_availability(stock_availability: int, amount: int):
        if (stock_availability < amount):
            raise ValueError('Stock is not sufficient')
        return True

    def validate_buy_order(stock: Stock, order: OrderBase):
        return OrderService.price_within_bound(price=stock.price, lower_bound=order.lower_bound, upper_bound=order.upper_bound) and OrderService.check_availability(stock_availability=stock.availability, amount=order.total)

    def validate_sell_order(stock: Stock, order: OrderBase):
        return OrderService.price_within_bound(price=stock.price, lower_bound=order.lower_bound, upper_bound=order.upper_bound)

    def buy(order: OrderCreate, db: Session):
        print(order)
        db_item = Order(**order, type=OrderTypeEnum.buy,
                        total=order["amount"] * order["unit_price"])
        db.add(db_item)
        return

    def sell(order: OrderCreate, db: Session):
        db_item = Order(**order.dict(), type=OrderTypeEnum.sell,
                        total=order.amount * order.unit_price)
        db.add(db_item)
        return
