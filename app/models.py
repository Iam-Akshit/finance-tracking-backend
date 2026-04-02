from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
import enum
from datetime import datetime
from .database import Base


class TransactionType(str, enum.Enum):
    income = "income"
    expense = "expense"


class UserRole(str, enum.Enum):
    viewer = "viewer"
    analyst = "analyst"
    admin = "admin"


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    role = Column(Enum(UserRole), default=UserRole.viewer)

    transactions = relationship("Transaction", back_populates="owner")


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    type = Column(Enum(TransactionType), nullable=False)
    category = Column(String, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    notes = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="transactions")