from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    accounts = relationship("Account", back_populates="owner")

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String, unique=True)
    balance = Column(Float, default=0.0)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="accounts")
    # Связь для входящих и исходящих транзакций
    sent_transactions = relationship("Transaction", foreign_keys="Transaction.sender_id")
    received_transactions = relationship("Transaction", foreign_keys="Transaction.receiver_id")

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    sender_id = Column(Integer, ForeignKey("accounts.id"))
    receiver_id = Column(Integer, ForeignKey("accounts.id"))
