import hashlib
import secrets

from prisma.models import EncryptionKey

from .repository import EncryptionKeyRepository


class EncryptionKeyService:
    """Contains the business logic for managing encryption keys."""

    def __init__(self, repository: EncryptionKeyRepository) -> None:
        self.repository = repository

    async def create_key(self, name: str, user_id: str) -> tuple[str, str]:
        """Create a new encryption key and return the client ID and secret."""
        client_id = f"sk_{secrets.token_urlsafe(16)}"
        client_secret = secrets.token_urlsafe(32)
        client_secret_hash = hashlib.sha256(client_secret.encode()).hexdigest()

        await self.repository.create(name, client_id, client_secret_hash, user_id)

        return client_id, client_secret

    async def validate_key(self, client_id: str, client_secret: str) -> bool:
        """Validate an encryption key."""
        key = await self.repository.find_by_client_id(client_id)
        if not key or key.revokedAt:
            return False

        client_secret_hash = hashlib.sha256(client_secret.encode()).hexdigest()
        return client_secret_hash == key.client_secret_hash

    async def list_keys_for_user(self, user_id: str) -> list[EncryptionKey]:
        """List all encryption keys for a user."""
        return await self.repository.find_by_user_id(user_id)

    async def revoke_key(self, key_id: str) -> EncryptionKey | None:
        """Revoke an encryption key."""
        return await self.repository.revoke_by_id(key_id)
