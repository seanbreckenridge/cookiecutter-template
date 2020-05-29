import io
from setuptools import setup, find_packages

requirements = []

# Use the README.md content for the long description:
with io.open('README.md', encoding='utf-8') as fo:
    long_description = fo.read()

setup(
    name='{{ cookiecutter.project_name }}',
    version="0.1.0",
    url=
    'https://gitlab.com/{{ cookiecutter.github_username }}/{{ cookiecutter.module_name }}',
    author='{{ cookiecutter.author_name }}',
    author_email='{{ cookiecutter.author_email }}',
    description=('''{{ cookiecutter.project_short_description }}'''),
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages(include=['{{cookiecutter.module_name}}']),
    test_suite='tests',
    install_requires=requirements,
    keywords='',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
)
