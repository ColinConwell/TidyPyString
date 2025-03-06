#!/bin/bash
# Script to run tests and publish the TidyPyString package to PyPI

set -e

# Define colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

# Helper function to print formatted messages
print_section() {
  echo -e "\n${GREEN}=== $1 ===${NC}"
}

print_error() {
  echo -e "\n${RED}❌ $1${NC}"
}

print_warning() {
  echo -e "${YELLOW}⚠️  $1${NC}"
}

print_success() {
  echo -e "${GREEN}✅ $1${NC}"
}

# Go to project root
cd "$(dirname "$0")/.."
ROOT_DIR=$(pwd)

# Check Git status
print_section "Checking Git Status"
if [[ -n $(git status --porcelain) ]]; then
  print_warning "You have uncommitted changes:"
  git status --short
  
  read -p "Continue anyway? (y/N): " response
  if [[ "$response" != "y" && "$response" != "Y" ]]; then
    print_error "Publishing cancelled - please commit or stash your changes first"
    exit 1
  fi
else
  print_success "Git repository is clean"
fi

# Poetry configuration check
print_section "Poetry Configuration Check"
if ! poetry check; then
  print_error "Poetry configuration check failed"
  exit 1
fi

# Install dependencies
print_section "Installing Dependencies"
if ! poetry install; then
  print_error "Failed to install dependencies"
  exit 1
fi

# Run tests if available (will be skipped if test command fails)
print_section "Running Tests"
if command -v pytest &> /dev/null; then
  if ! poetry run pytest; then
    print_error "Tests failed"
    exit 1
  else
    print_success "All tests passed"
  fi
else
  print_warning "pytest not found, skipping tests"
fi

# Linting check if available
print_section "Running Linting"
if command -v flake8 &> /dev/null; then
  if ! poetry run flake8 tidystring; then
    print_error "Linting failed"
    exit 1
  else
    print_success "Linting passed"
  fi
else
  print_warning "flake8 not found, skipping linting"
fi

# Type checking if available
print_section "Running Type Checking"
if command -v mypy &> /dev/null; then
  if ! poetry run mypy tidystring; then
    print_error "Type checking failed"
    exit 1
  else
    print_success "Type checking passed"
  fi
else
  print_warning "mypy not found, skipping type checking"
fi

# Build package
print_section "Building Package"
if ! poetry build; then
  print_error "Failed to build package"
  exit 1
fi
print_success "Package built successfully"

# Confirmation before publishing
print_section "Ready to Publish"
echo "All checks passed. Ready to publish to PyPI."
read -p "Do you want to publish to PyPI? (y/N): " response
if [[ "$response" != "y" && "$response" != "Y" ]]; then
  echo "Publishing cancelled."
  exit 0
fi

# Publish to PyPI
print_section "Publishing to PyPI"
if ! poetry publish; then
  print_error "Publishing failed"
  exit 1
fi

print_success "Package successfully published to PyPI!"
echo "You can view it at: https://pypi.org/project/tidystring/"