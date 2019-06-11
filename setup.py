"""Setup for wordsearch."""


# [ Imports ]
# [ -Python ]
from setuptools import setup, find_packages


# [ Main ]
setup(
    name="wordsearch",
    version="0.1.0",
    description="Generate and solve a word search graph.",
    url="https://github.com/danjchoi/WordSearch",
    author="danjchoi",
    author_email="danjchoi@umich.edu",
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    install_requires=["click"],
    extras_require={"testing": ["pytest"], "dev": ["black", "pytest"]},
    entry_points={"console_scripts": ["wordsearch=wordsearch.cli:cli"]},
)
