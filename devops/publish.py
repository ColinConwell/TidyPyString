#!/usr/bin/env python3
"""
Script to run tests and publish the TidyPyString package to PyPI.
Performs safety checks before publishing.
"""

import os
import sys
import subprocess
from pathlib import Path


def run_command(command, description):
    """Run a shell command and handle potential errors."""
    print(f"\n=== {description} ===")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"ERROR: {description} failed!")
        print(f"Output: {result.stdout}")
        print(f"Error: {result.stderr}")
        return False
    
    print(result.stdout)
    return True


def check_git_status():
    """Check if repository is clean (no uncommitted changes)."""
    print("\n=== Checking Git Status ===")
    result = subprocess.run(
        "git status --porcelain", 
        shell=True, 
        capture_output=True, 
        text=True
    )
    
    if result.stdout.strip():
        print("WARNING: You have uncommitted changes:")
        print(result.stdout)
        response = input("Continue anyway? (y/N): ")
        return response.lower() == 'y'
    
    print("Git repository is clean.")
    return True


def main():
    # Get the project root directory
    root_dir = Path(__file__).parent.parent
    os.chdir(root_dir)
    
    # 1. Check git status
    if not check_git_status():
        sys.exit(1)
    
    # 2. Run basic checks
    checks = [
        # Setup checks
        ("poetry check", "Poetry configuration check"),
        ("poetry install", "Installing dependencies"),
        
        # Code quality checks
        ("flake8 tidystring", "Linting with flake8"),
        ("black --check tidystring", "Code style check with black"),
        ("mypy tidystring", "Type checking with mypy"),
        
        # Tests (if pytest is used)
        ("pytest", "Running tests"),
    ]
    
    for command, description in checks:
        try:
            if not run_command(command, description):
                print("\n❌ Pre-publish checks failed. Fix the issues and try again.")
                sys.exit(1)
        except FileNotFoundError:
            print(f"WARNING: Command '{command.split()[0]}' not found. Skipping {description}.")
    
    # 3. Build the package
    if not run_command("poetry build", "Building package"):
        print("\n❌ Package build failed.")
        sys.exit(1)
    
    # 4. Confirm with user before publishing
    print("\n=== Ready to Publish ===")
    print("All checks passed. Ready to publish to PyPI.")
    response = input("Do you want to publish to PyPI? (y/N): ")
    
    if response.lower() != 'y':
        print("Publishing cancelled.")
        sys.exit(0)
    
    # 5. Publish to PyPI
    if not run_command("poetry publish", "Publishing to PyPI"):
        print("\n❌ Publishing failed.")
        sys.exit(1)
    
    print("\n✅ Package successfully published to PyPI!")


if __name__ == "__main__":
    main()