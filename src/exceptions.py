from fastapi import HTTPException, status


class UserNotFoundException(HTTPException):
    """Custom exception for when a user is not found."""

    def __init__(self) -> None:
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


class UserAlreadyExistsException(HTTPException):
    """Custom exception for when a user with the given email already exists."""

    def __init__(self) -> None:
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail="User with this email already exists")
