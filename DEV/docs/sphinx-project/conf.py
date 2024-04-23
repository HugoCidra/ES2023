# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Documentação do Backend, Testes Funcionais e Testes Unitários'
copyright = '2023, PL1'
author = 'PL1'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [ 'sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = '\\n'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Custom code to append to conf.py
import os
import sys
import django

sys.path.append(os.path.abspath('../../'))
sys.path.append(os.path.abspath('../../testing/'))
sys.path.append(os.path.abspath('../../backend/main/'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
django.setup()


