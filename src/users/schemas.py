from pydantic import BaseModel


class UserCreate(BaseModel):
    """Schema for creating a new user."""

    email: str
    name: str | None = None


class UserResponse(BaseModel):
    """Schema for responding with user data."""

    id: str
    email: str
    name: str | None = None

    class Config:
        """Pydantic configuration for ORM mode."""

        from_attributes = True
