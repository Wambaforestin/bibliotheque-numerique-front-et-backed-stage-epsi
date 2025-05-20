from app.models.user import UserCreate, UserLogin
from app.db.mongo import users
from app.core.security import get_password_hash, verify_password

def create_user(user: UserCreate):
    if users.find_one({"email": user.email}):
        return False
    hashed_password = get_password_hash(user.password)
    users.insert_one({"email": user.email, "hashed_password": hashed_password, "role": user.role})
    return True

def authenticate_user(user: UserLogin):
    db_user = users.find_one({"email": user.email})
    if not db_user:
        return None
    if not verify_password(user.password, db_user["hashed_password"]):
        return None
    return db_user
