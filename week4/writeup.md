# Week 4 Writeup: The Autonomous Coding Agent IRL

## 1. Design Inspiration
I chose to implement `CLAUDE.md` and a Custom Slash Command. The inspiration came from the Anthropic best practices documentation, specifically the need to set clear guardrails for AI tools (avoiding hallucinated commands) and automating repetitive CI/CD-like workflows locally to reduce developer friction.

## 2. Automations Built

### Automation A: Repository Guidance (`CLAUDE.md`)
*   **Goal:** Provide context-aware rules so the agent understands the FastAPI structure and enforces a Test-Driven Development (TDD) workflow.
*   **Inputs/Outputs:** Implicit. It reads the file on startup. Output is modified agent behavior (e.g., writing tests before code).
*   **Safety Notes:** Forces the agent to use safe, predefined `make` commands rather than guessing.

### Automation B: Custom Slash Command (`/test-lint`)
*   **Goal:** A single command to run formatting, linting, and testing sequentially.
*   **Steps:** Runs `make format` -> `make lint` -> `make test`. If any fail, it stops and suggests a fix.
*   **How to run:** Type `/test-lint` in the Claude Code prompt.
*   **Expected Output:** Either a success message indicating clean code, or a failure summary with a fix snippet.

## 3. Before vs. After
*   **Manual Workflow (Before):** I had to manually remind the AI about the project structure, tell it to write tests first, and manually type `make format`, `make lint`, and `make test` in the terminal every time I changed a file.
*   **Automated Workflow (After):** The AI already knows the TDD rules via `CLAUDE.md`. Verifying code quality is reduced to typing a single `/test-lint` command.

## 4. How you used the automation to enhance the starter application
I used these automations to add a new `/api/v1/health` endpoint to the FastAPI backend. 
First, because of the `CLAUDE.md` guardrails, when I prompted the agent to "add a health route", it automatically started by writing a failing test in `backend/tests/` without me explicitly asking for it. After it implemented the route, I simply typed `/test-lint`. The custom slash command automatically formatted the new code, ran the linter, executed pytest, and verified that my new endpoint was working perfectly.