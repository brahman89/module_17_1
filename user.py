from fastapi import APIRouter, HTTPException
from app_3.schemas import CreateUser, UpdateUser

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/")
async def all_users():
    pass

@router.get("/user_id")
async def user_by_id():
    pass


@router.post("/create", response_model=CreateUser)
async def create_user():
    """Create new user"""

    pass


@router.put("/update")
async def update_user():
    """Change information about user"""
    pass


@router.delete("/delete")
async def delete_user():
    pass
