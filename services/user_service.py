from fastapi import APIRouter, HTTPException,Query,Request,Body
from typing import List
# from models.user_model import User
from controllers.user_controller import UserController

# Initialize router
router = APIRouter()

@router.get("/get_all/")
async def get_all_user():
    return UserController.get_all()

@router.get("/get_by_id/{user_id}")
async def get_by_id(user_id: int):
    return UserController.get_by_id(str(user_id))

@router.post("/user/")
async def create_user(
    name: str = Body(..., example="John Doe"),
    email: str = Body(..., example="johndoe@example.com")
):
    try:
        # Create user
        created_user = UserController.create_user(name=name, email=email)
        return {
            "message": "User created successfully",
            "user": {
                "user_id": str(created_user.user_id),
                "name": created_user.name,
                "email": created_user.email,
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
