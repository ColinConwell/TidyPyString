# Configuration file for the Sphinx documentation builder.

# For the full list of built-in configuration values, see:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os, sys
sys.path.insert(0, os.path.abspath('../'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'tidypystring'
release = '0.1.0'
author = 'Colin Conwell'
#copyright = '2024, Colin Conwell'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'myst_parser',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

exclude_patterns = [
    'Thumbs.db',
    '_build',  
    '.DS_Store'
]

templates_path = ['_templates']

# autodoc_mock_imports = ['strings']

autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'undoc-members': True,
    # 'special-members': '__init__',
    'show-inheritance': True,
}

# Dictionary of autosummary settings
autosummary_settings = {
    'recursive': True,
    'generate': True,
    'imported_members': False,
    'ignore_module_all': True,
    'output_dir': 'generated',
    'generate_overwrite': True,
}

# Update globals with autosummary settings:
# globals().update(autosummary_settings)

# ... or define settings directly:
autosummary_generate = True
autosummary_imported_members = True
autosummary_recursive = True
autosummary_output_dir = 'modules'
autosummary_generate_overwrite = True


# napoleon autodoc settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True

# settings reference: https://github.com/cimarieta/sphinx-autodoc-example/

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_title = "TidyPyString Docs"

html_permalinks_icon = '<span>#</span>'
html_theme = 'sphinxawesome_theme'

html_static_path = ['_static']
html_js_files = ['_static/custom.js']

book_theme_options = {
    "repository_url": "https://github.com/ColinConwell/TidyPyString",
    "use_repository_button": True,
    # "path_to_docs": "sphinx/source",
    # "extra_footer": "Additional text to display at end of page",
}

# html_theme_options = book_theme_options

# -- Additional Formatting ----------------------------------------------------

add_module_names = False
python_use_unqualified_type_names = True
