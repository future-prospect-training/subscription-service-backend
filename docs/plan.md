# Refactoring Plan: Subscription Service Backend (Python Mirror)

This document outlines the step-by-step progression for refactoring the `subscription-service-backend` project into a modern, Pythonic application, mirroring the architectural principles of the provided NestJS project. The goal is to achieve a high-quality, production-ready backend using FastAPI, Poetry, and other best-in-class Python tools, while strictly adhering to Pythonic coding standards and file organization.

## Phase 1: Project Scaffolding & Core Setup

1.  **Initialize Project with Poetry:**
    *   Use Poetry as the dependency and environment manager.
    *   Run `poetry init` to create `pyproject.toml`.
    *   **Pythonic Note:** Poetry provides isolated environments and manages dependencies cleanly, aligning with Python best practices for project setup.

2.  **Create Basic Directory Structure:**
    *   Ensure `src/`, `tests/`, and `.env` are present.
    *   **Pythonic Note:** The `src/` directory is a common and recommended structure for Python packages, separating source code from other project files.

3.  **Install Core Dependencies:**
    *   `poetry add fastapi`
    *   `poetry add "uvicorn[standard]"` (ASGI server)
    *   `poetry add python-dotenv` (For loading .env files)
    *   `poetry add --group dev pytest httpx` (For testing)
    *   **Pythonic Note:** Using `poetry add` ensures dependencies are properly managed and recorded in `pyproject.toml` and `poetry.lock`.

4.  **Create Basic FastAPI App & Health Check:**
    *   In `src/main.py`, create a basic FastAPI app instance.
    *   Add a `/health` endpoint returning `{"status": "ok"}`.
    *   **Pythonic Note:** `main.py` serves as the primary entry point, and a health check is a standard practice for API readiness.

## Phase 2: Configuration and Database

1.  **Configuration Management (Pydantic Settings):**
    *   Install `pydantic-settings`: `poetry add pydantic-settings`.
    *   Create `src/config.py`.
    *   Define a `Settings` class using Pydantic's `BaseSettings` to read and validate environment variables from `.env`.
    *   **Pythonic Note:** Pydantic provides robust data validation and settings management, promoting type safety and clear configuration.

2.  **Database with Prisma (Direct Mirror):**
    *   Reuse the existing `prisma/schema.prisma` file.
    *   Install Prisma Client for Python: `poetry add prisma`.
    *   Run `poetry run prisma generate` to create the type-safe Python client.
    *   Create `src/database.py` to manage the Prisma client instance and provide it via FastAPI's dependency injection.
    *   **Pythonic Note:** Leveraging Prisma Python client maintains a consistent ORM approach, and `database.py` centralizes database connection logic.

## Phase 3: Building Features (Modular Architecture)

1.  **Modular Architecture with `APIRouter`:**
    *   Use FastAPI's `APIRouter` for modularity, similar to NestJS modules.
    *   For each feature (e.g., "Users"), create a dedicated directory: `src/users/`.
    *   Inside `src/users/`, create:
        *   `router.py`: Defines API routes (equivalent to NestJS controllers).
        *   `service.py`: Contains core business logic (equivalent to NestJS services).
        *   `schemas.py`: Defines Pydantic models for request/response data validation (equivalent to DTOs).
    *   In `src/main.py`, import and include feature routers.
    *   **Pythonic Note:** This structure promotes clear separation of concerns, reusability, and maintainability, aligning with Python's emphasis on modularity. File names are lowercase with underscores, following PEP 8.

## Phase 4: Middleware, Error Handling, and Tooling

1.  **Custom Error Handling:**
    *   Create `src/exceptions.py`.
    *   Use FastAPI's `@app.exception_handler()` decorator to catch specific exceptions (e.g., `UserNotFound`) and return standardized JSON error responses.
    *   **Pythonic Note:** Centralized exception handling ensures consistent error responses and improves API usability.

2.  **Middleware (e.g., Correlation ID):**
    *   Create `src/middleware.py`.
    *   Implement a middleware function to handle correlation IDs.
    *   Add this middleware to the FastAPI app instance in `main.py`.
    *   **Pythonic Note:** Middleware provides a clean way to inject cross-cutting concerns like logging or authentication.

3.  **Linting & Formatting:**
    *   Install `ruff`: `poetry add --group dev ruff`.
    *   Configure `ruff` in `pyproject.toml` for linting and formatting.
    *   **Pythonic Note:** `ruff` is a highly performant and Pythonic linter/formatter, ensuring code quality and adherence to PEP 8.

4.  **Git Hooks:**
    *   Use `pre-commit` framework: `poetry add --group dev pre-commit`.
    *   Run `poetry run pre-commit install`.
    *   Create `.pre-commit-config.yaml` to run `ruff` automatically before each commit.
    *   **Pythonic Note:** `pre-commit` hooks automate code quality checks, ensuring that only well-formatted and linted code is committed.

This plan will guide the refactoring process, ensuring a robust, maintainable, and Pythonic backend application.

---

## Next Steps Plan: Towards Production Readiness

**Phase 5: Advanced Features & Best Practices**

1.  **Implement Authentication and Authorization:**
    *   **Goal:** Secure API endpoints.
    *   **Action:** Integrate JWT-based authentication (e.g., using `python-jose` or `FastAPI-Users`). Implement FastAPI `Security` dependencies.

2.  **Logging and Monitoring:**
    *   **Goal:** Comprehensive and structured logging for debugging and operational insights.
    *   **Action:** Configure Python's `logging` module for structured logging (e.g., using `python-json-logger` or `loguru`). Integrate with a monitoring solution.

3.  **Testing (Comprehensive Suite):**
    *   **Goal:** Ensure correctness and prevent regressions.
    *   **Action:** Write unit tests for service/utility functions and integration tests for API endpoints using `httpx` and FastAPI's `TestClient`. Implement strategies for testing database interactions.

4.  **API Documentation (OpenAPI/Swagger UI):**
    *   **Goal:** Provide clear and interactive API documentation.
    *   **Action:** Ensure all endpoints, request bodies, and responses are properly documented using Pydantic models and docstrings.

5.  **Error Handling (Refinement):**
    *   **Goal:** Provide user-friendly and consistent error responses.
    *   **Action:** Expand `src/exceptions.py` with more specific custom exceptions. Implement global exception handlers for common HTTP errors.

**Phase 6: Deployment & Operations**

1.  **Containerization (Docker):**
    *   **Goal:** Consistent and reproducible deployment environment.
    *   **Action:** Refine `Dockerfile` for production (e.g., multi-stage builds, non-root user, optimized image size).

2.  **Environment Management:**
    *   **Goal:** Securely manage environment variables in production.
    *   **Action:** Ensure `.env` is only for local development. Use environment variables directly in production or a secrets management service.

3.  **CI/CD Pipeline:**
    *   **Goal:** Automate testing and deployment.
    *   **Action:** Set up a CI/CD pipeline (e.g., GitHub Actions, GitLab CI) to run tests, build Docker images, and deploy the application.

4.  **Performance Optimization:**
    *   **Goal:** Ensure the application is performant under load.
    *   **Action:** Consider caching strategies (e.g., Redis). Optimize database queries. Profile the application to identify bottlenecks.

5.  **Security Hardening:**
    *   **Goal:** Protect against common web vulnerabilities.
    *   **Action:** Implement CORS policies. Validate all input. Use secure headers. Regularly update dependencies.

**Phase 7: Continuous Improvement**

1.  **Monitoring and Alerting:**
    *   **Goal:** Proactively identify and respond to issues.
    *   **Action:** Set up monitoring dashboards and alerts for key metrics.

2.  **Documentation (User & Developer):**
    *   **Goal:** Maintain clear and up-to-date documentation.
    *   **Action:** Expand `README.md` with deployment instructions, API usage, and development guidelines.