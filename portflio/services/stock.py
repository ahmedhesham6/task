from uuid import UUID
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from models import Stock


class StockService:

    def find_by_id(stock_id: UUID, db: Session):
        try:
            stock = db.query(Stock).filter(
                Stock.stock_id == stock_id).one()
            return stock
        except NoResultFound:
            raise ValueError('Stock does not exists')
