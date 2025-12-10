.PHONY: help install test test-cov lint format check clean run scaffold pre-commit-install pre-commit-run

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'
	@echo ''
	@echo 'Run with arguments: ./run.py --help'

install: ## Install dependencies
	uv sync

pre-commit-install: ## Install pre-commit hooks
	uv run pre-commit install
	uv run pre-commit install --hook-type pre-push

pre-commit-run: ## Run pre-commit on all files
	uv run pre-commit run --all-files

test: ## Run all tests
	uv run pytest -v

test-cov: ## Run tests with coverage report
	uv run pytest --cov=src --cov-report=term-missing --cov-report=html

lint: ## Run linter (with auto-fix)
	uv run ruff check . --fix

format: ## Format code
	uv run ruff format .

check: format lint test ## Run format, lint, and test

clean: ## Remove cache and build artifacts
	rm -rf .pytest_cache .ruff_cache htmlcov .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

run: ## Run with arguments (e.g., make run ARGS="--latest")
	uv run python run.py $(ARGS)

scaffold: ## Create new solution structure (e.g., make scaffold YEAR=2025 DAY=8)
	@if [ -z "$(YEAR)" ] || [ -z "$(DAY)" ]; then \
		echo "Error: YEAR and DAY are required"; \
		echo "Usage: make scaffold YEAR=2025 DAY=8"; \
		exit 1; \
	fi
	uv run python scripts/scaffold.py $(YEAR) $(DAY)

.DEFAULT_GOAL := help
