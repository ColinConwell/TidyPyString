#!/bin/bash
# Simple script to format Python code using Black

# Navigate to the repository root directory (parent of this script's directory)
cd "$(dirname "$0")/.."

# Check if Black is installed, install if needed
if ! command -v black &> /dev/null; then
    echo "Black not found, installing..."
    pip install black
fi

# Set options
LINE_LENGTH=120

# Run Black formatter
echo "Formatting Python code with Black (line length: $LINE_LENGTH)..."
black --line-length $LINE_LENGTH tidystring/

echo "✅ Code formatting complete!"