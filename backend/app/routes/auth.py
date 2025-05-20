from fastapi import APIRouter, HTTPException, Depends
from pymongo.collection import Collection

from app.models.user import UserCreate, UserLogin
from app.services.user_service import create_user, authenticate_user
from app.core.security import create_access_token, get_current_user
from app.dependencies import get_users_collection  # ✅ indispensable

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    if create_user(user):
        return {"msg": "Utilisateur créé"}
    raise HTTPException(status_code=400, detail="Utilisateur existe déjà")

@router.post("/login")
def login(user: UserLogin):
    authenticated_user = authenticate_user(user)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Identifiants invalides")
    token = create_access_token({"sub": authenticated_user['email'], "role": authenticated_user['role']})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/stats")
def user_stats(
    users: Collection = Depends(get_users_collection),
    user: dict = Depends(get_current_user)
):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Accès interdit")
    
    pipeline = [
        {"$group": {"_id": "$role", "count": {"$sum": 1}}}
    ]
    return {doc["_id"]: doc["count"] for doc in users.aggregate(pipeline)}
