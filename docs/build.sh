#!/bin/bash

# Install dependencies if needed
if [ "$1" == "install" ]; then
    pip install -e ..
    pip install sphinx sphinx-rtd-theme myst-parser sphinx-autodoc-typehints
fi

# Clean & build the HTML
make clean && make html

echo "Documentation built successfully in _build/html"
echo "Open _build/html/index.html in your browser to view"