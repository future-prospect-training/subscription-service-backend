from prisma.models import User
from src.database import db
from src.users.schemas import UserCreate


class UserService:
    """Service class for user-related operations."""

    async def create_user(self, user_data: UserCreate) -> User:
        """Create a new user in the database."""
        return await db.user.create(data=user_data.model_dump())

    async def get_user_by_id(self, user_id: str) -> User | None:
        """Retrieve a user by their ID."""
        return await db.user.find_unique(where={"id": user_id})

    async def get_user_by_email(self, email: str) -> User | None:
        """Retrieve a user by their email address."""
        return await db.user.find_unique(where={"email": email})
