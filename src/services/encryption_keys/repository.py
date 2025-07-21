from datetime import datetime, timezone
from prisma import Prisma
from prisma.models import EncryptionKey

class EncryptionKeyRepository:
    """Handles data access for the EncryptionKey model."""

    def __init__(self, db: Prisma) -> None:
        self.db = db

    async def create(self, name: str, client_id: str, client_secret_hash: str, user_id: str) -> EncryptionKey:
        """Create a new encryption key."""
        return await self.db.encryptionkey.create(
            data={
                "name": name,
                "client_id": client_id,
                "client_secret_hash": client_secret_hash,
                "userId": user_id,
            }
        )

    async def find_by_client_id(self, client_id: str) -> EncryptionKey | None:
        """Find an encryption key by its client ID."""
        return await self.db.encryptionkey.find_unique(where={"client_id": client_id})

    async def find_by_user_id(self, user_id: str) -> list[EncryptionKey]:
        """Find all encryption keys for a user."""
        return await self.db.encryptionkey.find_many(where={"userId": user_id})

    async def revoke_by_id(self, key_id: str) -> EncryptionKey | None:
        """Revoke an encryption key by its ID."""
        return await self.db.encryptionkey.update(
            where={"id": key_id},
            data={"revokedAt": datetime.now(timezone.utc)},
        )