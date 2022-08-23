from sqlalchemy import Column, Numeric, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from db.database import Base


class Balance(Base):
    __tablename__ = "balances"
    user_id = Column(UUID(as_uuid=True), primary_key=True)
    deposits = Column(Numeric(10, 2))
    withdraws = Column(Numeric(10, 2))
    balance = Column(Numeric(10, 2))
