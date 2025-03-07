# TidyPyString Documentation

This directory contains the Sphinx documentation for the TidyPyString package.

## Documentation Structure

The documentation is organized thematically:

- **overview.md**: Overview of the package and its features
- **string_basics.rst**: Basic string operations (length, padding, etc.)
- **string_detection.rst**: Functions for detecting patterns in strings
- **string_extraction.rst**: Functions for extracting parts of strings
- **string_modification.rst**: Functions for modifying and transforming strings
- **string_case.rst**: Case conversion functions
- **string_utilities.rst**: Utility functions for working with strings
- **advanced_usage.rst**: Advanced usage patterns and examples
- **api-ref.rst**: Auto-generated API reference

## Building the Documentation

To build the documentation:

1. Ensure you have the necessary dependencies installed:
   ```bash
   pip install sphinx sphinx-rtd-theme myst-parser sphinx-autodoc-typehints sphinxawesome-theme
   ```

2. Build the documentation using the build script:
   ```bash
   ./build.sh
   ```

3. If you need to install dependencies first:
   ```bash
   ./build.sh install
   ```

4. View the built documentation by opening `_build/html/index.html` in your browser.

## Adding New Documentation

To add new documentation:

1. Create a new `.rst` or `.md` file in the `source/` directory
2. Add the file to the table of contents in `source/index.rst`
3. Run the build script to generate the documentation

## Folder Structure

- `source/`: Documentation source files
- `_templates/`: Custom Sphinx templates
- `_static/`: Static files (CSS, JavaScript, etc.)
- `_build/`: Generated documentation (after building)