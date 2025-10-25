# -- Project information -----------------------------------------------------
project = "ROSConDE 2025 Navigation Workshop"
author = "Philipp & Team"
release = "2025.10"
html_title = "ROSConDE 2025 Navigation Workshop"

# -- General config ----------------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_design",
]

myst_enable_extensions = ["colon_fence"]

templates_path = ["_templates"]
exclude_patterns = ["_build"]

# -- HTML theme --------------------------------------------------------------
html_theme = "furo"
html_static_path = ["_static"]

# Copybutton: ignore prompts in code blocks
copybutton_prompt_text = r">>> |\$ |ros2 "
copybutton_prompt_is_regexp = True

# Optional: If you later add a logo:
# html_logo = "_static/logo.png"
