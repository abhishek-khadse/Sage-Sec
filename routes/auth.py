from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from typing import Optional
from pydantic import BaseModel
from ..utils.security import (
    verify_password,
    get_password_hash,
    create_access_token,
    get_current_active_user
)
from ..main import app

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    full_name: Optional[str] = None

class UserUpdate(BaseModel):
    email: Optional[str] = None
    full_name: Optional[str] = None
    password: Optional[str] = None

class Token(BaseModel):
    access_token: str
    token_type: str

@router.post("/register", response_model=Token)
async def register(user: UserCreate):
    """Register a new user"""
    # Check if username exists
    existing_user = await app.mongodb.users.find_one({"username": user.username})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )

    # Create new user
    hashed_password = get_password_hash(user.password)
    user_dict = user.dict()
    user_dict.pop("password")
    user_dict["hashed_password"] = hashed_password
    user_dict["disabled"] = False

    # Save to database
    result = await app.mongodb.users.insert_one(user_dict)
    user_dict["_id"] = str(result.inserted_id)

    # Create access token
    access_token_expires = timedelta(minutes=app.settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """Login user and return access token"""
    user = await app.mongodb.users.find_one({"username": form_data.username})
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=app.settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]},
        expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get("/me")
async def read_users_me(current_user: dict = Depends(get_current_active_user)):
    """Get current user information"""
    return current_user

@router.put("/me")
async def update_user(
    user_update: UserUpdate,
    current_user: dict = Depends(get_current_active_user)
):
    """Update current user information"""
    update_data = user_update.dict(exclude_unset=True)
    if "password" in update_data:
        update_data["hashed_password"] = get_password_hash(update_data.pop("password"))

    await app.mongodb.users.update_one(
        {"username": current_user["username"]},
        {"$set": update_data}
    )

    return {"message": "User updated successfully"} 