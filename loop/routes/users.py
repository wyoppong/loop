from typing import List
from fastapi import APIRouter, Depends, Path

from loop.app.models.user import User_Pydantic, UserIn_Pydantic, User
from loop.app.enums import Tags

router = APIRouter(prefix="/users", tags=[Tags.users])


@router.get("/", status_code=200, response_model=List[User_Pydantic], response_description="All users of the system")
async def index():
    """
    Get All Users
    """
    return await  User_Pydantic.from_queryset(User.all())

@router.post("/create", response_model=User_Pydantic, response_description="New user created")
async def create_user(user: UserIn_Pydantic):
    """
    Create User
    """
    user_obj = await User.create(**user.dict(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)