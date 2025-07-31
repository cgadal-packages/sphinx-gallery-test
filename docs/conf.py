# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# Below is only needed if the module is not installed in the environement.
# If it is not, you can either uncomment the line below, or install it using "pip3 install -e ./"
# It is mandatory if you want compilation using github actions
sys.path.insert(0, os.path.abspath("../"))

# -- Project information -----------------------------------------------------

project = "mytoolbox"
copyright = "2021, Cyril Gadal"
author = "Cyril Gadal"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",  # Core Sphinx library for auto html doc generation from docstrings
    "sphinx.ext.autosummary",  # Create neat summary tables for modules/classes/methods etc
    # Link to other project's documentation (see mapping below)
    "sphinx.ext.intersphinx",
    # Add a link to the Python source code for classes, functions etc.
    "sphinx.ext.viewcode",
    # Automatically document param types (less noise in class signature)
    "sphinx_autodoc_typehints",
    # 'nbsphinx',  # Integrate Jupyter Notebooks and Sphinx
    "sphinx.ext.napoleon",
    "numpydoc",
    "sphinx.ext.doctest",
    "sphinx.ext.mathjax",
    "sphinx_gallery.gen_gallery",
    "sphinx.ext.coverage",
]

autosummary_generate = True  # Turn on sphinx.ext.autosummary
autosummary_imported_members = True  # Also documents imports in __init__.py
# autoclass_content = "both"  # Add __init__ doc (ie. params) to class summaries
# Remove 'view source code' from top of page (for html, not python)
html_show_sourcelink = False
autodoc_inherit_docstrings = True  # If no docstring, inherit from base class
# Enable 'expensive' imports for sphinx_autodoc_typehints
set_type_checking_flag = True
nbsphinx_allow_errors = True  # Continue through Jupyter errors
# autodoc_typehints = "description" # Sphinx-native method. Not as good as sphinx_autodoc_typehints
add_module_names = False  # Remove namespaces from class/method signatures

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"
highlight_language = "python3"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for Sphinx gallery ---------------------------------------------

intersphinx_mapping = {
    "python": (f"https://docs.python.org/{sys.version_info.major}", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
}

examples_dirs = ["../examples"]
gallery_dirs = ["_examples"]

sphinx_gallery_conf = {
    "examples_dirs": examples_dirs,  # path to your example scripts
    "gallery_dirs": gallery_dirs,  # path to where to save gallery generated output
    # directory where function/class granular galleries are stored
    "backreferences_dir": "_gen_modules/backreferences",
    # Modules for which function/class level galleries are created.
    "doc_module": ("mytoolbox"),
    "reference_url": {
        "mytoolbox": None,  # The module you locally document uses None
        "numpy": "https://docs.scipy.org/doc/numpy/",
        "matplotlib": "https://matplotlib.org/stable",
    },
    "matplotlib_animations": True,
    "plot_gallery": True,
    "filename_pattern": "example",
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Pydata theme
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "show_prev_next": False,
    "logo": {
        "text": "pyudv",
    },
    "github_url": "https://github.com/cgadal-packages/sphinx-gallery-test",
}

html_static_path = ["_static"]
html_css_files = ["pydata-custom.css"]

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False
html_copy_source = False
