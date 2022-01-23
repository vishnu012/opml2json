import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="opml2json",
    version="0.0.3",
    description="convert opml to json",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/vishnu012/opml2json",
    author="Vishnu",
    author_email="vishnu012@pm.me",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["opml2json"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "vishnu=opml2json.__main__:main",
        ]
    },
)