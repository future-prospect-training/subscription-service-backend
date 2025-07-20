import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pythonjsonlogger import jsonlogger

from src.auth.router import router as auth_router
from src.config import settings
from src.database import connect_db, disconnect_db
from src.middleware import CorrelationIdMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Handle startup and shutdown events for the application."""
    # Configure logging
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter("%(asctime)s %(levelname)s %(name)s %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(settings.log_level)

    await connect_db()
    yield
    await disconnect_db()


app = FastAPI(lifespan=lifespan)

app.add_middleware(CorrelationIdMiddleware)
app.include_router(auth_router)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """Handle HTTP exceptions and return a JSON response."""
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


@app.get("/health")
async def health_check() -> dict:
    """Return the health status of the application."""
    return {"status": "ok"}
