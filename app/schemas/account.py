"""Account request/response schemas"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


class AccountType(str, Enum):
    """Account type enumeration"""
    CHECKING = "checking"
    SAVINGS = "savings"
    INVESTMENT = "investment"


class AccountCreate(BaseModel):
    """Account creation schema"""
    account_type: AccountType = AccountType.CHECKING
    currency: str = "USD"


class AccountResponse(BaseModel):
    """Account response schema"""
    id: int
    user_id: int
    account_number: str
    account_type: str
    balance: float
    currency: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class AccountUpdate(BaseModel):
    """Account update schema"""
    is_active: Optional[bool] = None
