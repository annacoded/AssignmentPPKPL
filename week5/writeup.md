# Week 5 Writeup: Agentic Development with Warp

## 1. Automations Built

### Automation A: Warp Drive Saved Prompt (Test & Lint Harness)
* **Goal:** Provide a reusable, one-click prompt in Warp Drive to execute formatting, linting, and testing sequentially for the FastAPI backend.
* **Inputs/Outputs:** Input is the saved prompt triggered from Warp's AI command search. Output is a clean terminal execution of the `make` commands, stopping only if an error occurs to provide a suggested fix.
* **Autonomy Level:** Medium. The agent executes safe read/test commands but waits for my approval before modifying any code based on test failures.

### Automation B: Multi-Agent Workflow (Concurrent Tasks)
* **Goal:** Utilize separate Warp tabs to run independent agents working on the repository concurrently without clobbering each other.
* **Roles & Coordination Strategy:** * **Tab 1 (Backend Agent):** Tasked with generating a new health-check endpoint logic in `backend/app/`.
    * **Tab 2 (Docs Agent):** Tasked with reading `/openapi.json` and updating `docs/API.md`.
* **Concurrency Wins/Risks:** The major win is speed; I can generate code and documentation simultaneously. The risk is file lock conflicts if both agents try to write to the same file (e.g., both updating `main.py`). I mitigated this by strictly isolating their working directories (one strictly in `backend/`, the other strictly in `docs/`).

## 2. Before vs. After
* **Manual Workflow (Before):** Context switching was a nightmare. I had to write backend code, wait for tests to finish, and only then start manually updating the API documentation.
* **Automated Workflow (After):** Using Warp's multi-tab agentic features, I act as an orchestrator. I trigger the saved test-runner prompt in one tab, while instructing another tab to update the documentation in parallel.

## 3. How I Used the Automation (Pain Point Resolved)
This setup drastically accelerates the development lifecycle. The Warp Drive saved prompt eliminates the repetitive typing of CI/CD-like commands. Meanwhile, the multi-agent workflow resolves the bottleneck of sequential development. By isolating agents into separate tabs with distinct boundaries, I can achieve parallel execution of disparate tasks (like coding and documenting) safely within a single machine.