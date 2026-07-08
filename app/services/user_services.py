from app.schemas.user import UserCreate, UserResponse
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User
from sqlalchemy.exc import IntegrityError

users_db = []
next_user_id = 1

class EmailAlreadyExistsError(Exception):
    pass

def create_user(user: UserCreate, db: Session) -> UserResponse:
   
    new_user = User(
    
        name=user.name,
        email=user.email
    )
    
    db.add(new_user)
    try:
        db.commit()
    except IntegrityError as error:
        db.rollback()
        raise EmailAlreadyExistsError() from error
    db.refresh(new_user)
  

    return new_user

def get_all_users(db: Session) -> list[User]:
    statement = select(User)
    users = db.scalars(statement).all()
    return users

def get_user_by_id(user_id: int, db: Session) -> User:
    user = db.get(User, user_id) 
    
    return user

   

def delete_user(id: int, db: Session):

    user = db.get(User, id)
    if user is not None:
        db.delete(user)
        db.commit()
        return True
    else:
        return False




 