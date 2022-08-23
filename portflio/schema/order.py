from typing import List, Optional
from pydantic import BaseModel
from uuid import UUID


class OrderBase(BaseModel):
    stock_id: UUID
    user_id: UUID
    total: int
    upper_bound: float
    lower_bound: float


class OrderCreate(BaseModel):
    stock_id: UUID
    user_id: UUID
    amount: int
    unit_price: float
