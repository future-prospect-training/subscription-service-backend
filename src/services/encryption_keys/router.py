from fastapi import APIRouter, Depends, HTTPException
from prisma import Prisma
from src.database import get_db
from src.users.models import User
from src.auth.utils import get_current_active_user
from .service import EncryptionKeyService
from .repository import EncryptionKeyRepository
from pydantic import BaseModel, Field
from typing import List

class Key(BaseModel):
    """Represents an encryption key."""
    id: str
    name: str
    client_id: str
    created_at: str = Field(alias="createdAt")
    revoked_at: str | None = Field(alias="revokedAt")

class NewKey(BaseModel):
    """Represents a new encryption key."""
    client_id: str
    client_secret: str

router = APIRouter()

@router.post("/keys", status_code=201, response_model=NewKey)
async def create_key(
    name: str,
    db: Prisma = Depends(get_db),
    user: User = Depends(get_current_active_user),
) -> NewKey:
    """Create a new encryption key."""
    repository = EncryptionKeyRepository(db)
    service = EncryptionKeyService(repository)
    client_id, client_secret = await service.create_key(name, user.id)
    return NewKey(client_id=client_id, client_secret=client_secret)

@router.get("/keys", response_model=List[Key])
async def list_keys(
    db: Prisma = Depends(get_db),
    user: User = Depends(get_current_active_user),
) -> List[Key]:
    """List all encryption keys for the current user."""
    repository = EncryptionKeyRepository(db)
    service = EncryptionKeyService(repository)
    keys = await service.list_keys_for_user(user.id)
    return [Key.model_validate(key) for key in keys]

@router.delete("/keys/{key_id}", status_code=204)
async def revoke_key(
    key_id: str,
    db: Prisma = Depends(get_db),
    user: User = Depends(get_current_active_user),
) -> None:
    """Revoke an encryption key."""
    repository = EncryptionKeyRepository(db)
    service = EncryptionKeyService(repository)
    key = await service.revoke_key(key_id)
    if not key or key.userId != user.id:
        raise HTTPException(status_code=404, detail="Key not found")