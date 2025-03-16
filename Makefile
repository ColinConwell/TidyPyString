.PHONY: install dev test lint docs clean build publish

# Default target
all: test lint docs

# Install the package
install:
	pip install -e .

# Install development dependencies
dev:
	pip install hatch
	hatch env create

# Run tests
test:
	hatch run test:run

# Run test coverage
coverage:
	hatch run test:cov

# Run linting
lint:
	hatch run lint:check

# Format code
format:
	hatch run lint:style

# Build documentation
docs:
	hatch run docs:build

# Serve documentation locally
docs-serve:
	hatch run docs:serve

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf coverage.xml
	hatch run docs:clean
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name "*.pyc" -delete

# Build package
build:
	hatch build

# Publish package to PyPI
publish:
	hatch publish

# Enter development shell
shell:
	hatch shell 