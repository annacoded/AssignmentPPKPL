# Name: test-lint
# Intent: Run all tests and formatting checks, then summarize the results.

Run the following commands strictly in this order:
1. `make format`
2. `make lint`
3. `make test`

If any step fails, stop immediately, summarize the exact failure, and provide a code snippet to fix it. If all pass, output a success message saying "All checks passed! Your FastAPI code is clean."