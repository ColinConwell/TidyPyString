#!/bin/bash
# Simple script to check code quality without modifying files

# Navigate to the repository root directory (parent of this script's directory)
cd "$(dirname "$0")/.."

# Check if Black is installed, install if needed
if ! command -v black &> /dev/null; then
    echo "Black not found, installing..."
    pip install black
fi

# Set options
LINE_LENGTH=120

# Check formatting with Black (doesn't modify files)
echo "Checking code formatting with Black (line length: $LINE_LENGTH)..."
black --check --line-length $LINE_LENGTH tidystring/

if [ $? -eq 0 ]; then
    echo "✅ Code formatting check passed!"
else
    echo "❌ Code formatting issues found. Run './devops/format.sh' to fix."
fi