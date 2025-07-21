from fastapi import APIRouter, Depends, HTTPException
from prisma import Prisma
from src.database import get_db
from src.users.models import User
from src.auth.utils import get_current_active_user
from .service import EncryptionKeyService
from .repository import EncryptionKeyRepository

router = APIRouter()

@router.post("/keys", status_code=201)
async def create_key(
    name: str,
    db: Prisma = Depends(get_db),
    user: User = Depends(get_current_active_user),
):
    repository = EncryptionKeyRepository(db)
    service = EncryptionKeyService(repository)
    client_id, client_secret = await service.create_key(name, user.id)
    return {"client_id": client_id, "client_secret": client_secret}

@router.get("/keys")
async def list_keys(
    db: Prisma = Depends(get_db),
    user: User = Depends(get_current_active_user),
):
    repository = EncryptionKeyRepository(db)
    service = EncryptionKeyService(repository)
    return await service.list_keys_for_user(user.id)

@router.delete("/keys/{key_id}")
async def revoke_key(
    key_id: str,
    db: Prisma = Depends(get_db),
    user: User = Depends(get_current_active_user),
):
    repository = EncryptionKeyRepository(db)
    service = EncryptionKeyService(repository)
    key = await service.revoke_key(key_id)
    if not key or key.userId != user.id:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"message": "Key revoked"}
