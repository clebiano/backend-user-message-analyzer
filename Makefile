###
# Docker section
###
build: ## Docker: Initialize project
	docker compose build

run:
	docker compose run --service-ports -e --rm api bash -c "uvicorn app.main:app --host 0.0.0.0 --port 8000"

run-tests: ## Docker: Run tests
	docker compose run --service-ports --no-deps --rm api bash -c "pytest /app"
