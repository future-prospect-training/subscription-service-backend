# Subscription Service Backend

This project is a Python-based backend service for managing subscriptions, built with Flask and SQLAlchemy.

## Features

*   **RESTful API:** Implements CRUD operations for subscriptions and users.
*   **Database Migrations:** Uses Flask-Migrate and Alembic for database schema management.
*   **API Documentation:** Integrated with Flask-RESTX for interactive Swagger UI documentation.
*   **Authentication:** Basic JWT authentication for securing API endpoints.
*   **Structured Logging:** Configured with `python-json-logger` for better log analysis.
*   **Error Handling:** Custom exception classes and centralized error handling for consistent API responses.
*   **Containerization:** Dockerfile included for easy deployment.

## Setup

### Prerequisites

*   Docker (for running the local database)
*   Python 3.8+
*   `pip` for dependency management

### Local Development Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd subscription-service-backend
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**

    Create a `.env` file in the project root with the following content:

    ```
    SECRET_KEY=your_super_secret_key
    DATABASE_URL=postgresql://postgres:mysecretpassword@localhost:5432/postgres
    JWT_SECRET_KEY=your_jwt_secret_key
    ```

    *Replace `your_super_secret_key` and `your_jwt_secret_key` with strong, randomly generated values.*

5.  **Start the local PostgreSQL database:**

    ```bash
    bash start_local_db.sh
    ```

    This will start PostgreSQL and pgAdmin containers.

6.  **Initialize and run database migrations:**

    ```bash
    set -a; . ./.env; set +a; export FLASK_APP=run.py && flask db upgrade
    ```

    *If this is the first time running migrations, you might need to initialize first:*

    ```bash
    set -a; . ./.env; set +a; export FLASK_APP=run.py && flask db init
    set -a; . ./.env; set +a; export FLASK_APP=run.py && flask db migrate -m "Initial migration."
    set -a; . ./.env; set +a; export FLASK_APP=run.py && flask db upgrade
    ```

7.  **Run the application:**

    ```bash
    python run.py
    ```

    The API will be accessible at `http://localhost:3000`.

## API Documentation

Access the interactive API documentation (Swagger UI) at `http://localhost:3000/` once the application is running.

## Running Tests

To run the tests:

```bash
set -a; . ./.env; set +a; pytest
```

## Docker

### Build the Docker image

```bash
docker build -t subscription-service-backend .
```

### Run the Docker container

```bash
docker run -p 3000:3000 --env-file ./.env subscription-service-backend
```
