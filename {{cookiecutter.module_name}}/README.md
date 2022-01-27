# {{ cookiecutter.module_name }}

{{ cookiecutter.project_short_description }}

## Installation

Requires `python3.7+`

To install with pip, run:

    pip install {{ cookiecutter.module_name }}

---

## Usage

```
TODO: Fill this out

Usage: ...
```

### Tests

```bash
git clone 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.module_name }}'
cd ./{{ cookiecutter.module_name }}
pip install '.[testing]'
mypy ./{{ cookiecutter.module_name }}
pytest
```
