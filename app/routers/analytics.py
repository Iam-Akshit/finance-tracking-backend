from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud, database, auth

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get("/summary", response_model=schemas.AnalyticsSummary)
def get_summary(
    db: Session = Depends(database.get_db),
    user_id: int = Depends(auth.get_current_user_id),
    role: str = Depends(auth.require_analyst_or_admin) # Only Analyst/Admin can view analytics
):
    return crud.get_financial_summary(db=db, user_id=user_id)