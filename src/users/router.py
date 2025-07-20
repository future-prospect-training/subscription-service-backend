from typing import Annotated

from fastapi import APIRouter, Depends, status

from src.exceptions import UserAlreadyExistsException, UserNotFoundException
from src.users.schemas import UserCreate, UserResponse
from src.users.service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate, user_service: Annotated[UserService, Depends()]) -> UserResponse:
    """Create a new user."""
    if await user_service.get_user_by_email(user_data.email):
        raise UserAlreadyExistsException
    return await user_service.create_user(user_data)


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str, user_service: Annotated[UserService, Depends()]) -> UserResponse:
    """Retrieve a user by ID."""
    if not (user := await user_service.get_user_by_id(user_id)):
        raise UserNotFoundException
    return user
