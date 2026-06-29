# Repository Guidance for Developer Command Center (Week 4)

## Architecture
- Backend: FastAPI (located in `backend/`).
- Database: SQLite via SQLAlchemy.
- Frontend: Static HTML/JS/CSS (located in `frontend/`).

## Style & Guardrails
- **Tooling Expectations:** We use `black` and `ruff` for formatting and linting.
- **Workflow:** When asked to add a new API endpoint, ALWAYS follow these steps:
  1. Write a failing test in `backend/tests/` first (TDD approach).
  2. Implement the route in `backend/app/`.
  3. Run `make format` and `make lint`.
  4. Run `make test` to verify.

## Commands
- Run app: `make run`
- Run tests: `make test`
- Lint: `make lint`