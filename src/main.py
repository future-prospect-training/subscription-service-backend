from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database import connect_db, disconnect_db
from src.middleware import CorrelationIdMiddleware
from src.users.router import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Handle startup and shutdown events for the application."""
    await connect_db()
    yield
    await disconnect_db()


app = FastAPI(lifespan=lifespan)

app.add_middleware(CorrelationIdMiddleware)
app.include_router(users_router)


@app.get("/health")
async def health_check() -> dict:
    """Return the health status of the application."""
    return {"status": "ok"}
