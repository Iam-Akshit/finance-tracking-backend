from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import schemas, crud, database, auth

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/", response_model=schemas.TransactionResponse, status_code=status.HTTP_201_CREATED)
def create_transaction(
    transaction: schemas.TransactionCreate,
    db: Session = Depends(database.get_db),
    user_id: int = Depends(auth.get_current_user_id),
    role: str = Depends(auth.require_admin) # Only Admins can create in this spec
):
    return crud.create_transaction(db=db, transaction=transaction, user_id=user_id)

@router.get("/", response_model=List[schemas.TransactionResponse])
def read_transactions(
    skip: int = 0,
    limit: int = 100,
    transaction_type: Optional[schemas.TransactionType] = None,
    category: Optional[str] = None,
    db: Session = Depends(database.get_db),
    user_id: int = Depends(auth.get_current_user_id)
):
    return crud.get_transactions(
        db, user_id=user_id, skip=skip, limit=limit,
        transaction_type=transaction_type, category=category
    )

@router.delete("/{transaction_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_transaction(
    transaction_id: int,
    db: Session = Depends(database.get_db),
    user_id: int = Depends(auth.get_current_user_id),
    role: str = Depends(auth.require_admin)
):
    deleted = crud.delete_transaction(db, transaction_id=transaction_id, user_id=user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return None