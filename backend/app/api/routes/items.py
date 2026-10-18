from fastapi import APIRouter, Depends
from app.core.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/")
def get_items(db: Session = Depends(get_db)):
    return {"items": [], "message": "Items endpoint ready"}