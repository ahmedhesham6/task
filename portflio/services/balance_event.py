from uuid import UUID
from sqlalchemy.orm import Session
from models import Balance, BalanceEvent, BalanceEventTypeEnum
from schema import BalanceEventBase
from .balance import BalanceService


class BalanceEventService:

    def deposit(user_id: UUID, amount: float, db: Session):
        db_item = BalanceEvent(user_id=user_id, type=BalanceEventTypeEnum.deposit,
                               amount=amount)
        db.add(db_item)
        return

    def withdraw(user_id: UUID, amount: float, db: Session):
        if BalanceService.enough_amount_exist(user_id=user_id, amount=amount, db=db):
            db_item = BalanceEvent(user_id=user_id, type=BalanceEventTypeEnum.withdraw,
                                   amount=amount)
            db.add(db_item)
        return
