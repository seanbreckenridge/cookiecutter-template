# cookiecutter-template

Custom cookiecutter template for my defaults. Uses parts of the [default](https://github.com/audreyr/cookiecutter-pypackage).

* uses `click` for handling CLI arguments
* creates a `__main__.py` file to be executed like `python -m modulename`.
* Sets up [`pytest`](https://docs.pytest.org/en/latest/) (with an `.ini` file to run doctests) and `mypy`
* `setup.py` sets up a typed package, and reads from the `requirements.txt` and `README.md` for dependencies/long_description

Run:

```
cookiecutter gh:seanbreckenridge/cookiecutter-template
cd package_name
pip install '.[testing]'
pytest
```
