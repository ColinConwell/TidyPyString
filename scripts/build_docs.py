#!/usr/bin/env python3
"""
Build documentation for TidyPyString.
Run this script from the project root directory.
"""

import os
import subprocess
import sys
from pathlib import Path

def main():
    """Build the documentation using Sphinx."""
    # Get the project root directory
    project_root = Path(__file__).parent.parent.absolute()
    docs_dir = project_root / "docs"
    
    # Check if docs directory exists
    if not docs_dir.exists():
        print(f"Error: Documentation directory not found at {docs_dir}")
        sys.exit(1)
    
    # Change to the docs directory
    os.chdir(docs_dir)
    
    # Build HTML documentation
    print("Building HTML documentation...")
    result = subprocess.run(
        ["sphinx-build", "-b", "html", ".", "_build/html"],
        capture_output=True,
        text=True,
    )
    
    if result.returncode != 0:
        print("Error building documentation:")
        print(result.stderr)
        sys.exit(1)
    
    print(f"Documentation built successfully. Output in {docs_dir}/_build/html")
    print("To view the documentation, open the following file in your browser:")
    print(f"file://{docs_dir}/_build/html/index.html")

if __name__ == "__main__":
    main() 