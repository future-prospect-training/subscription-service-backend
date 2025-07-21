from prisma import Prisma

db = Prisma()


async def connect_db() -> None:
    """Connect to the database."""
    await db.connect()


async def disconnect_db() -> None:
    """Disconnects from the database."""
    await db.disconnect()
