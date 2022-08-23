from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel


class BalanceEventBase(BaseModel):
    user_id: UUID
    amount: float
