from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas
from datetime import datetime


def create_transaction(db: Session, transaction: schemas.TransactionCreate, user_id: int):
    db_transaction = models.Transaction(
        **transaction.model_dump(exclude_unset=True),
        user_id=user_id
    )
    if not db_transaction.date:
        db_transaction.date = datetime.utcnow()

    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def get_transactions(
        db: Session,
        user_id: int,
        skip: int = 0,
        limit: int = 100,
        transaction_type: Optional[models.TransactionType] = None,
        category: Optional[str] = None
):
    query = db.query(models.Transaction).filter(models.Transaction.user_id == user_id)

    if transaction_type:
        query = query.filter(models.Transaction.type == transaction_type)

    if category:
        query = query.filter(models.Transaction.category == category)

    return query.offset(skip).limit(limit).all()

def delete_transaction(db: Session, transaction_id: int, user_id: int):
    db_transaction = db.query(models.Transaction).filter(
        models.Transaction.id == transaction_id,
        models.Transaction.user_id == user_id
    ).first()

    if db_transaction:
        db.delete(db_transaction)
        db.commit()
    return db_transaction


def get_financial_summary(db: Session, user_id: int):
    # Calculate totals
    income = db.query(func.sum(models.Transaction.amount)).filter(
        models.Transaction.user_id == user_id,
        models.Transaction.type == models.TransactionType.income
    ).scalar() or 0.0

    expense = db.query(func.sum(models.Transaction.amount)).filter(
        models.Transaction.user_id == user_id,
        models.Transaction.type == models.TransactionType.expense
    ).scalar() or 0.0

    # Calculate category breakdown
    category_data = db.query(
        models.Transaction.category, func.sum(models.Transaction.amount)
    ).filter(models.Transaction.user_id == user_id).group_by(models.Transaction.category).all()

    breakdown = {cat: amt for cat, amt in category_data}

    return {
        "total_income": income,
        "total_expense": expense,
        "current_balance": income - expense,
        "category_breakdown": breakdown
    }