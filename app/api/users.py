from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user import UserCreate, UserResponse
from app.services import user_services
from sqlalchemy.orm import Session
from app.db import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_services.create_user(user, db)


@router.get("", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    users = user_services.get_all_users(db)
    return users


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int,  db: Session = Depends(get_db)):
    user = user_services.get_user_by_id(user_id, db)

    

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int):
    deleted = user_services.delete_user(user_id)
    
    if not deleted:
        raise HTTPException(
            status_code=404,
            details="User Not Found"
        )