import uuid
import enum
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Numeric, Integer, String, Enum, DATETIME, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base


class OrderTypeEnum(enum.Enum):
    buy = "buy"
    sell = "sell"


class Order(Base):
    __tablename__ = "orders"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False,
                primary_key=True, index=True)
    stock_id = Column(UUID(as_uuid=True), ForeignKey('stocks.stock_id'))
    user_id = Column(UUID(as_uuid=True))
    type = Column(Enum(OrderTypeEnum))
    amount = Column(Integer)
    unit_price = Column(Numeric(10, 2))
    total = Column(Numeric(10, 2))
    timestamp = Column(DATETIME, default=func.now())

    stock = relationship("Stock")
