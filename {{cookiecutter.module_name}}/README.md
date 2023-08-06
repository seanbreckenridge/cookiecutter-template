# {{ cookiecutter.module_name }}

{{ cookiecutter.project_short_description }}

## Installation

Requires `python3.8+`

To install with pip, run:

```
pip install git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.module_name }}
```

## Usage

```
{{ cookiecutter.module_name }} --help
```

### Tests

```bash
git clone 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.module_name }}'
cd ./{{ cookiecutter.module_name }}
pip install '.[testing]'
pytest
flake8 ./{{ cookiecutter.module_name }}
mypy ./{{ cookiecutter.module_name }}
```
