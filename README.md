# Subscription Service Backend

This project is a modern Python-based backend service for managing subscriptions, built with FastAPI, Poetry, and Prisma.

## Features

*   **FastAPI Framework:** High-performance, easy-to-use web framework.
*   **Poetry for Dependency Management:** Ensures reproducible builds and clean dependency management.
*   **Prisma ORM:** Type-safe database access and migrations.
*   **Modular Architecture:** Organized into features (e.g., `users`) using FastAPI's `APIRouter`.
*   **Pydantic for Data Validation:** Robust data validation and serialization.
*   **Custom Error Handling:** Consistent and user-friendly error responses.
*   **Correlation ID Middleware:** For improved request tracing and logging.
*   **Ruff for Linting & Formatting:** Ensures code quality and adherence to Pythonic standards.
*   **Pre-commit Hooks:** Automates code quality checks before commits.
*   **Containerization:** Docker Compose setup for local development database.

## Setup

### Prerequisites

*   [Docker](https://docs.docker.com/get-docker/) (for running the local database)
*   [Poetry](https://python-poetry.org/docs/#installation) (for dependency management)
*   Python 3.12+

### Local Development Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd subscription-service-backend
    ```

2.  **Install dependencies using Poetry:**

    ```bash
    poetry install
    ```

3.  **Set up environment variables:**

    Create a `.env` file in the project root with the following content:

    ```
    DATABASE_URL="postgresql://postgres:mysecretpassword@localhost:5432/postgres"
    # Add other environment variables as needed, e.g., for authentication
    ```

    *Note: The `DATABASE_URL` should match the configuration in `docker-compose.yml`.*

4.  **Start the local PostgreSQL database:**

    ```bash
    docker-compose up -d
    ```

    This will start a PostgreSQL container.

5.  **Apply Prisma database migrations:**

    ```bash
    poetry run prisma migrate dev --name init
    ```

    This will create the necessary tables in your local database.

6.  **Run the application:**

    ```bash
    poetry run uvicorn src.main:app --reload
    ```

    The API will be accessible at `http://127.0.0.1:8000`.

## API Documentation

FastAPI automatically generates interactive API documentation (Swagger UI) at `http://127.0.0.1:8000/docs` and ReDoc documentation at `http://127.0.0.1:8000/redoc` once the application is running.

## Running Tests

To run the tests (once implemented):

```bash
poetry run pytest
```

## Docker

### Build the Docker image

```bash
docker build -t subscription-service-backend .
```

### Run the Docker container

```bash
docker run -p 8000:8000 --env-file ./.env subscription-service-backend
```

## Future Plans

For a detailed roadmap and future development plans, please refer to `docs/plan.md`.