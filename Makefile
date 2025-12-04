.PHONY: help install test test-cov lint format check clean run

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'
	@echo ''
	@echo 'Run with arguments: ./run.py --help'

install: ## Install dependencies
	uv sync

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

.DEFAULT_GOAL := help
