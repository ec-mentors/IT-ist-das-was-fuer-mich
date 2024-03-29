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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import datetime

# -- Project information -----------------------------------------------------

project = "IT, ist das was für mich?"
copyright = f"{datetime.date.today().year}, everyone codes"
author = "Rea Sutter, Claus Aichinger and everyonecodes"

# https://sphinx-book-theme.readthedocs.io/en/latest/customize/sidebar-primary.html
html_title = "Arbeitsmaterialien für Berufsorientierung IT"
html_logo = "_static/ec_logo.png"
html_favicon = "_static/ec_favicon.png"

# https://sphinx-book-theme.readthedocs.io/en/latest/customize/sidebar-primary.html#customize-the-sidebar-footer
# https://sphinx-book-theme.readthedocs.io/en/latest/customize/index.html?highlight=footer#theme-options
AMS_LOGO_HTML = """
Im Auftrag des
<a href="http://www.ams.at/wien"><img src="https://www.ams.at/_images/900_logo_news.jpg" alt="Im Auftrag des AMS Wien"></a>
"""

html_theme_options = {
    "extra_navbar": AMS_LOGO_HTML,
    # "extra_footer": AMS_LOGO_HTML,  # looks too clunky
}

# -- Project data ------------------------------------------------------------
from textwrap import dedent
# Substitutions replace
# With regards to links, see https://myst-parser.readthedocs.io/en/latest/syntax/optional.html?highlight=admonition#substitutions-and-urls
myst_substitutions = {
    #
    "doc_Berufe_und_Kurse": "https://docs.google.com/document/d/1vORYLDeZEz7u5dMc9WX6z2KzeS2PVfcRDErXGQS_MQU/edit?usp=sharing",
    "ask_for_feedback": dedent("""
    ```{exercise} Feedback (10 Minuten)

    Wie war(en) die Woche(n) für dich?

    Bitte teile deine Gedanken mit uns, in dem du
    eine kleine Umfrage ausfüllst, danke: {{ feedback_link }}.
    ```
    """),
}



# -- General configuration ---------------------------------------------------

# The code for the language the docs are written in. Any text automatically generated by Sphinx will be in that language.
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-internationalization
language = 'de'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
import sys
import os
sys.path.append(os.path.abspath("./_ext"))
# TODO: remove unused
extensions = [
    # Custom
    # "feedback",
    # Standard
    "myst_parser",
    "sphinx_togglebutton",  # https://sphinx-togglebutton.readthedocs.io/
    # TODO: include once exercises are there
    "sphinx_exercise",  # https://github.com/executablebooks/sphinx-exercise
    "sphinx_tabs.tabs",  # https://github.com/executablebooks/sphinx-tabs
    "sphinx_copybutton",  # https://github.com/executablebooks/sphinx-copybutton
    "sphinxemoji.sphinxemoji",  # https://github.com/sphinx-contrib/emojicodes
]

# MyST extensions
myst_enable_extensions = [
    "html_image",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#syntax-images
    "linkify",  # to render raw links as html links
    "substitution",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html?highlight=admonition#substitutions-with-jinja2
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.

# Work in progress (wip) patterns for content that is not yet
# read for publication
wip_exclude_patterns = [
    "source/course/wip",
    "**/*wip*",
    "*wip*",  #  to exclude folders/files in source/*wip*
    "./source/participants/wip",
    "./source/course/wip",
]

# Permanent exclusion patterns for content that is never to be published
permanent_exclude_patterns = [
    # templates
    "course/_peer_learning.md",

    "**/day_xx_template/*",
    # slides
    "**/slides.md",
    # builds
    "_build",
    # interal and private todo notes
    "**/todo.md",
    "**/internal.md",
    "**/*private*",
]

# TODO: rethink this
# SPHINXOPTS="-t dev" is passed on command line
# print(tags)
# Note that `render_all_and_check_link.sh` builds the development or work in progress (wip) version
# of the website whereas the CI service only builds publication-ready-content.
# See how the `exclude_patterns` is specified in `conf.py`. The toggle is
# implemented using [`tags` passed to the build commands](https://www.sphinx-doc.org/en/master/usage/configuration.html#conf-tags).
# When we run sphinx using the "dev" tag, we also include
# content that is work in progress
if tags.has('dev'):
    exclude_patterns = permanent_exclude_patterns
else:
    exclude_patterns = permanent_exclude_patterns + wip_exclude_patterns

exclude_patterns = permanent_exclude_patterns + wip_exclude_patterns
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"  # https://github.com/executablebooks/sphinx-book-theme

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# -- Linkcheck ---------------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html?highlight=linkcheck#options-for-the-linkcheck-builder
linkcheck_ignore = [
    r'https://microbit.org/join',
    r'https://www.mipumi.com/',
    r'https://www.waveshare.com/piano-for-micro-bit.htm',
    r'https://www.waveshare.com/media/catalog/product/cache/1/thumbnail/122x122/9df78eab33525d08d6e5fb8d27136e95/p/i/piano-for-micro-bit-4.jpg',
    r'https://abo-jugend.at/',
    r'https://www.spengergasse.at/',
    r'https://www.udemy.com/',
]
