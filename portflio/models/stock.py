from sqlalchemy import Column, Numeric, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from db.database import Base


class Stock(Base):
    __tablename__ = "stocks"
    stock_id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String, unique=False, index=True)
    price = Column(Numeric(10, 2))
    availability = Column(Integer)
    max_day = Column(Numeric(10, 2))
    min_day = Column(Numeric(10, 2))
    max_hour = Column(Numeric(10, 2))
    min_hour = Column(Numeric(10, 2))
