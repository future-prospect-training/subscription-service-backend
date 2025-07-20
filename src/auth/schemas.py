from fastapi_users import schemas


class UserRead(schemas.BaseUser[str]):
    """Schema for reading user data."""

    name: str | None = None


class UserCreate(schemas.BaseUserCreate):
    """Schema for creating a new user."""

    name: str | None = None


class UserUpdate(schemas.BaseUserUpdate):
    """Schema for updating an existing user."""

    name: str | None = None
