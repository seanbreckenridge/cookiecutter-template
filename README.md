# cookiecutter-template

Custom cookiecutter template for my defaults. Uses parts of the [default](https://github.com/audreyr/cookiecutter-pypackage).

- uses `click` for handling CLI arguments
- creates a `__main__.py` file to be executed like `python -m modulename`.
- Puts all the declarative metadata (pytest, mypy, flake8, package metadata, requirements) in `setup.cfg`

Run:

```
cookiecutter gh:seanbreckenridge/cookiecutter-template
cd package_name
pip install '.[testing]'
pytest
```
