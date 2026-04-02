from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from .models import TransactionType, UserRole

class TransactionBase(BaseModel):
    amount: float = Field(..., gt=0, description="Amount must be greater than 0")
    type: TransactionType
    category: str
    date: Optional[datetime] = None
    notes: Optional[str] = None

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True

class AnalyticsSummary(BaseModel):
    total_income: float
    total_expense: float
    current_balance: float
    category_breakdown: dict