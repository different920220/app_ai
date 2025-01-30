# setup.py
import glob
import setuptools
from typing import List
import poker_ai


def get_scripts_from_bin() -> List[str]:
    """Get all local scripts from bin so they are included in the package."""
    return glob.glob("bin/*")


def get_package_description() -> str:
    """Returns a description of this package from the markdown files."""
    with open("README.md", "r") as stream:
        readme: str = stream.read()
    with open("HISTORY.md", "r") as stream:
        history: str = stream.read()
    return f"{readme}\n\n{history}"


def get_requirements() -> List[str]:
    """Returns all requirements for this package."""
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
    return requirements


setuptools.setup(
    name="poker_ai",  # The name of the package
    version=poker_ai.__version__,  # Version from the poker_ai module
    author="Leon Fedden, Colin Manko",  # Author name(s)
    author_email="leonfedden@gmail.com",  # Author email
    description="Open source implementation of a CFR based poker AI player.",  # Short description of your package
    long_description=get_package_description(),  # Long description, typically from your README
    long_description_content_type="text/markdown",  # The content type of your long description (Markdown)
    url="https://github.com/fedden/poker_ai",  # Project's home page URL
    packages=setuptools.find_packages(),  # Automatically discover and include all packages in the project
    install_requires=get_requirements(),  # List of dependencies from the requirements.txt file
    classifiers=[  # Classifiers help others discover your package by categorizing it
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    scripts=get_scripts_from_bin(),  # Include scripts from the bin directory in your package
    python_requires=">=3.7",  # Specify the Python version requirement
)
