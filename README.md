# cookiecutter-template

Custom cookiecutter template for my defaults. Uses parts of the [default](https://github.com/audreyr/cookiecutter-pypackage).

- uses [`click`](https://pypi.org/project/click/) for handling CLI arguments
- creates a `__main__.py` file to be executed like `python -m modulename`.
- Puts all the declarative metadata (pytest, mypy, flake8, package metadata, requirements) in `setup.cfg`

I use this both for CLI tools and libraries, I prefer to structure everything as a package as that means the code is always marked with a `py.typed` (meaning, mypy can figure out this code has types) file.

If I'm just doing a library, I delete the `__main__.py`, modify the `setup.cfg` to remove `click` and remove the `console_script` entry

Otherwise, I put code in some other file like `package_name/core.py`, and then import it in `__main__.py`

After `pip install cookiecutter`, run:

```bash
cookiecutter gh:seanbreckenridge/cookiecutter-template
cd ./package_name
pip install '.[testing]'
python3 -m pytest
```
