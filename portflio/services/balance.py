from uuid import UUID
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from models import Balance, BalanceEvent, BalanceEventTypeEnum, balance
from schema import BalanceEventBase


class BalanceService:

    def enough_amount_exist(user_id: UUID, amount: float, db: Session):
        user_balance = BalanceService.find_by_id(user_id=user_id, db=db)
        if (user_balance.balance < amount):
            raise ValueError('Balance is not enough')
        return True

    def find_by_id(user_id: UUID, db: Session):
        try:
            user_balance = db.query(Balance).filter(
                Balance.user_id == user_id).one()
            return user_balance
        except NoResultFound:
            raise ValueError('Balance does not exists')
