from fastapi import Header, HTTPException, Depends
from .models import UserRole

# Mocking a user context based on headers
def get_current_user_id(x_user_id: int = Header(..., description="Simulated User ID")):
    return x_user_id

def get_user_role(x_user_role: str = Header(..., description="Role: viewer, analyst, admin")):
    role = x_user_role.lower()
    if role not in [r.value for r in UserRole]:
        raise HTTPException(status_code=400, detail="Invalid role in header")
    return role

def require_admin(role: str = Depends(get_user_role)):
    if role != UserRole.admin.value:
        raise HTTPException(status_code=403, detail="Admin permissions required")
    return role

def require_analyst_or_admin(role: str = Depends(get_user_role)):
    if role not in [UserRole.admin.value, UserRole.analyst.value]:
        raise HTTPException(status_code=403, detail="Analyst or Admin permissions required")
    return role