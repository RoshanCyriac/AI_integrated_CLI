.PHONY: help install install-dev test clean build publish format lint check

help: ## Show this help message
	@echo "AI-shell - AI-Powered Interactive Shell"
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install the package in development mode
	pip install -e .

install-dev: ## Install the package with development dependencies
	pip install -e ".[dev]"

test: ## Run the test suite
	python -m pytest tests/ -v

clean: ## Clean build artifacts
	rm -rf build/ dist/ *.egg-info/ .pytest_cache/ .mypy_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean ## Build the package
	python -m build

publish: build ## Build and publish to PyPI (requires twine)
	twine upload dist/*

format: ## Format code with black
	black .

lint: ## Run linting checks
	flake8 .
	black --check .

check: ## Run all quality checks
	black --check .
	flake8 .
	mypy ai_shell/

all: clean lint test build ## Run all checks and build 