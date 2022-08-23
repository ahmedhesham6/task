import enum
import uuid
from sqlalchemy import Column, Numeric, Integer, String, Enum, DATETIME
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db.database import Base


class BalanceEventTypeEnum(enum.Enum):
    withdraw = "withdraw"
    deposit = "deposit"


class BalanceEvent(Base):
    __tablename__ = "balance_events"
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False,
                primary_key=True, index=True)
    user_id = Column(UUID(as_uuid=True))
    type = Column(Enum(BalanceEventTypeEnum))
    amount = Column(Numeric(10, 2))
    timestamp = Column(DATETIME, default=func.now())
