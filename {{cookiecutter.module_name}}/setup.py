import io
from setuptools import setup, find_packages

requirements = ["click>=7.0"]

# Use the README.md content for the long description:
with io.open("README.md", encoding="utf-8") as fo:
    long_description = fo.read()

setup(
    name="{{ cookiecutter.module_name }}",
    version="0.1.0",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.module_name }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    description=("""{{ cookiecutter.project_short_description }}"""),
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    packages=find_packages(include=["{{cookiecutter.module_name}}"]),
    test_suite="tests",
    install_requires=requirements,
    keywords="",
    entry_points={
        "console_scripts": [
            "{{cookiecutter.module_name}} = {{cookiecutter.module_name}}.__main__:main"
        ]
    },
    extras_require={
        "testing": [
            "pytest",
            "mypy",
        ]
    },
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
