from app.schemas.user import UserCreate, UserResponse


users_db = []
next_user_id = 1


def create_user(user: UserCreate) -> UserResponse:
    global next_user_id

    new_user = {
        "id": next_user_id,
        "name": user.name,
        "email": user.email
    }

    users_db.append(new_user)
    next_user_id += 1

    return new_user

def get_all_users() -> UserResponse:
    return users_db

def get_user_by_id(user_id: int) -> UserResponse:
    for user in users_db:
        if user["id"] == user_id:
            return user

    return None

def delete_user(user_id: int):

    global users_db

    for user in users_db:
        if user["id"] == user_id:
            users_db.remove(user)
            return True

    return False