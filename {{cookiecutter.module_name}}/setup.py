from pathlib import Path
from setuptools import setup, find_packages

long_description = Path("README.md").read_text()
reqs = Path("requirements.txt").read_text().strip().splitlines()

pkg = "{{ cookiecutter.module_name }}"
setup(
    name=pkg,
    version="0.1.0",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.module_name }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    description=("""{{ cookiecutter.project_short_description }}"""),
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(include=[pkg]),
    install_requires=reqs,
    package_data={pkg: ["py.typed"]},
    zip_safe=False,
    keywords="",
    python_requires=">=3.7",
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
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
