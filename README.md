# cookiecutter-template

Custom cookiecutter template for my defaults. Uses parts of the [defualt](https://github.com/audreyr/cookiecutter-pypackage), and [asweigarts](https://github.com/asweigart/cookiecutter-basicpythonproject).

Is a pypi-python module, uses `click` for handling CLI arguments, creates a `__main__.py` file to be executed like `python -m modulename`. Also sets up [pytest](https://docs.pytest.org/en/latest/), [travis](https://travis-ci.org/), has a `Makefile`, and `MANIFEST.in` with some shortcuts/defaults.

Run:

```
cookiecutter gh:seanbreckenridge/cookiecutter-template
cd package_name
make install
python3 -m pytest
```
