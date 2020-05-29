# cookiecutter-template

Custom cookiecutter template for my defaults. Uses parts of the [defualt](https://github.com/audreyr/cookiecutter-pypackage), and [asweigarts](https://github.com/asweigart/cookiecutter-basicpythonproject).

Is a pypi-python module, uses [pytest](https://docs.pytest.org/en/latest/), [travis](https://travis-ci.org/), and [pipenv](https://github.com/pypa/pipenv), has a `Makefile`, and `MANIFEST.in` with some shortcuts/defaults.

Run:

```
cookiecutter gh:seanbreckenridge/cookiecutter-template
cd package_name
pipenv install --dev
pipenv shell
make install
python3 -m pytest
```