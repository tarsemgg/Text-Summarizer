import setuptools

# Read the long description from the README file
with open("Readme.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Package version
__version__ = "0.0.0"

# Metadata
REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "TARSEMGG"
SRC_REPO = "text_summerizer"
AUTHOR_EMAIL = "tarsemj7@gmail.com"

# Setup function for setuptools
setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A simple Python library for summarizing large text documents.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"": "src"},  # Fixed the typo here
    packages=setuptools.find_packages(where="src"),  # Finds packages in the 'src' directory
)
