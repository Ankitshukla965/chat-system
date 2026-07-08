from app.schemas.user import UserCreate, UserResponse
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User

users_db = []
next_user_id = 1


def create_user(user: UserCreate, db: Session) -> UserResponse:
   
    new_user = User(
    
        name=user.name,
        email=user.email
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
  

    return new_user

def get_all_users(db: Session) -> UserResponse:
    statement = select(User)
    users = db.scalars(statement).all()
    return users

def get_user_by_id(user_id: int, db: Session) -> UserResponse:
    user = db.get(User, user_id) 
    
    return user

   

def delete_user(user_id: int):

    global users_db

    for user in users_db:
        if user["id"] == user_id:
            users_db.remove(user)
            return True

    return False