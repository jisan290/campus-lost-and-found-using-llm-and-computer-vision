from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import create_access_token, create_refresh_token, is_allowed_email
from app.schemas.schemas import UserCreate, UserLogin, Token
from slowapi import Limiter
from slowapi.util import get_remote_address

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)

@router.post("/register", response_model=Token)
@limiter.limit("5/minute")
async def register(request: Request, user_data: UserCreate, db: Session = Depends(get_db)):
    if not is_allowed_email(user_data.email):
        raise HTTPException(
            status_code=403,
            detail=f"Only @bracu.ac.bd email addresses are allowed"
        )
    # Full implementation in next step
    return {"message": "Registration endpoint ready"}

@router.post("/login", response_model=Token)
@limiter.limit("10/minute")
async def login(request: Request, credentials: UserLogin, db: Session = Depends(get_db)):
    # Full implementation in next step
    return {"message": "Login endpoint ready"}