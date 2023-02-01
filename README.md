# template_python_project

A template repository for Python projects. The project is setup with:
* A `.gitignore` to exclude Python, Jupyter notebooks and VS code's artifacts.
* Instructions for cloning the repository, and setting up a virtual environment,
with required packages for linting, documentation and unit testing.
* Sphinx documentation already set up.
* Pytest and tests folder for unit testing.
* Pylint for static code analysis.

The template also comes with documentation on several topics:
* Version control with Git
* Python virtual environment setup
* Writing documentation with Sphinx
* Writing unit tests with Pytest

## Using this template repository to setup a new repository

**Refer to the [checklist](./docs/source/checklist_new_project.md) when using
this template repository.**

Clone this repository:

```bash
# Move to a convenient location (e.g.: cd where/to/clone/this/repo)
https://github.com/Th-Havy/template_python_project.git
```

Move inside this repository and re-initialize the git repository
```bash
# Rename the root folder of the repository
mv template_python_project my_project_name
cd my_project_name
# Delete hidden .git folder
rm -rf .git/
# Initialize a new git repository
git init
```


```bash
git remote add origin https://github.com/<path/to/your/repo>git
```

Delete the irrelevant files from your repository, make some modifications and
push them to your own GitLab repository:

```bash
# git add <file1> <file2> ...
# git commit -m "Deleted irrelevant files + <description of your modifications>"

# Your principal branch could also be named main (use 'git push origin main')
git push origin master
```

## Dependencies

* `Python`: Use the most recent version (`3.9`).
* [Sphinx](https://www.sphinx-doc.org/en/master/): Python documentation tool
    * [sphinx-rtd-theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/):
    nice readable theme for the documentation.
    * [myst-parser](https://myst-parser.readthedocs.io/en/latest/sphinx/intro.html):
    to write sphinx documentation in Markdown instead of ReStructuredText.
* [PyTest](https://docs.pytest.org/): Python testing framework
* [Pylint](https://pylint.org/): Linter (static code analysis tool)

## Authors

* **Thomas Havy**
