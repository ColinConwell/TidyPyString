#!/bin/bash
# Script to test GitHub Actions workflow locally using act

# Navigate to the repository root directory (parent of this script's directory)
cd "$(dirname "$0")/.."

# Set environment variables
export PYPI_TOKEN="fake_token_for_testing"

echo "=== Running GitHub Actions workflow locally ==="
echo "Note: Linting, type checking and tests are non-blocking"

# Run the GitHub Actions workflow locally
# This will run all steps except the actual publishing to PyPI
act workflow_dispatch --container-architecture linux/amd64 -s PYPI_TOKEN=$PYPI_TOKEN

# Exit with the same status code as the act command
exit $?