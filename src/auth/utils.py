import os
from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy

from src.auth.schemas import UserRead
from src.database import db


class User(UserRead):
    """Represents a user in the application."""


class UserManager(UUIDIDMixin, BaseUserManager[User, str]):
    """Manages user-related operations."""

    async def on_after_register(self, user: User, request: Request | None = None) -> None:
        """Call after a user successfully registers."""
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(self, user: User, token: str, request: Request | None = None) -> None:
        """Call after a user requests a password reset."""
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(self, user: User, token: str, request: Request | None = None) -> None:
        """Call after a user requests email verification."""
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_db() -> AsyncGenerator[db.user, None]:
    """Yield the Prisma user client."""
    yield db.user


async def get_user_manager(user_db: Annotated[db.user, Depends(get_user_db)]) -> AsyncGenerator[UserManager, None]:
    """Yield the user manager."""
    yield UserManager(user_db)


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    """Return a JWT strategy for authentication."""
    return JWTStrategy(secret=os.environ["SECRET"], lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, str](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
