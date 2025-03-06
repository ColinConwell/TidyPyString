# TidyPyString DevOps

This directory contains scripts and tools for development, testing, and publishing.

## Available Scripts

### `run_format.sh`
Formats Python code using Black.
```bash
./run_format.sh
```

### `run_lint.sh`
Checks code formatting without modifying files.
```bash
./run_lint.sh
```

### `test_workflow.sh`
Tests the GitHub Actions workflow locally using `act`.
```bash
./test_workflow.sh
```

### `publish.sh`
Manual script for publishing to PyPI (interactive, requires confirmation).
```bash
./publish.sh
```

### `publish.py`
Python implementation of the publish script with additional checks.
```bash
python publish.py
```

## GitHub Actions Workflow

The project uses GitHub Actions for automated testing and publishing. The workflow is defined in `.github/workflows/publish.yml`.

### How to Publish

1. **Automatic publishing on release**:
   - Create a new GitHub Release
   - The workflow will run automatically and publish to PyPI

2. **Manual publishing**:
   - Go to the Actions tab in the GitHub repository
   - Select the "Publish to PyPI" workflow
   - Click "Run workflow"
   - Set "Publish to PyPI" to true
   - Click "Run workflow"

3. **Local testing**:
   - Run the test workflow script: `./test_workflow.sh`
   - This uses `act` to run the workflow locally

### Required Secrets

The workflow requires a PyPI API token to be configured in GitHub repository secrets as `PYPI_TOKEN`.

To set up the token:
1. Generate a token on PyPI (pypi.org) with upload permissions
2. Add it to your GitHub repository secrets with the name `PYPI_TOKEN`