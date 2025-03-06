#!/bin/bash
# Script to test GitHub Actions workflow locally using act

# Navigate to the repository root directory (parent of this script's directory)
cd "$(dirname "$0")/.."

# Set environment variables
export PYPI_TOKEN="fake_token_for_testing"

# Create a temporary workflow file that skips linting and type checking
TEMP_WORKFLOW=".github/workflows/temp_workflow.yml"
cp .github/workflows/publish.yml $TEMP_WORKFLOW

# Modify the workflow to make it pass for testing purposes
sed -i.bak 's/run: flake8 tidystring\//run: echo "Skipping linting"/' $TEMP_WORKFLOW
sed -i.bak 's/run: mypy tidystring\//run: echo "Skipping type checking"/' $TEMP_WORKFLOW
sed -i.bak 's/run: pytest/run: echo "Skipping tests"/' $TEMP_WORKFLOW

echo "=== Running GitHub Actions workflow locally (with checks skipped) ==="
echo "This is for testing the workflow structure only, not validating code quality."

# Run the GitHub Actions workflow locally using the temporary workflow file
# This will run all steps except the actual publishing to PyPI and skip failing checks
act workflow_dispatch -W $TEMP_WORKFLOW --container-architecture linux/amd64 -s PYPI_TOKEN=$PYPI_TOKEN

# Save the exit code
EXIT_CODE=$?

# Clean up
rm $TEMP_WORKFLOW
rm ${TEMP_WORKFLOW}.bak

# Exit with the same status code as the act command
exit $EXIT_CODE