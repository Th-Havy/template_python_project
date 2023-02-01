# Python virtual environment

## Goal

A Python virtual environments is an isolated environment containing its own 
python interpreter, and its own packages and dependencies.

The goal of using a virtual environment is twofold:
1. Have a reproducible Python environment, easily installed on any computer.
2. Explicitely keep track of the packages on which the project depends.

## Creating a new environment

```bash
# Always use the most recent python version (3.9), unless specific dependencies
# require an older version.
conda create -n <name_of_env> python=3.9
conda activate <name_of_env>

# Update pip within the virtual environment
python -m pip install --upgrade pip

# Installed the required packages for the repository
pip install -r requirements.txt
```

## Activating the environment

Everytime you open a new terminal, you must reactivate the virtual environment:
```bash
conda activate <name_of_env>
```

This will make sure that the correct version of Python is used, and that the
Python packages installed in the virtual environment are used within this
terminal.

If you want to deactivate it, use the command:
```bash
conda deactivate
```

## Installing packages

Always use `pip install` to install packages, and not `conda install`, so as not
to mix these two package managers.

To install a package, use the command:

```bash
pip install <name_of_package>
```

**After installing a package, make sure to add it to your `requirements.txt`.**
The requirements should always be up to date, so that other collaborators can
easily install/update their virtual environment.

If `requirements.txt` was update by someone else you will need to update yours.
Most of the time re-running `pip install -r requirements.txt` (after having
activated your virtual environment) is enough to include the newly added
packages. However, you might sometimes need to delete the old environment and 
re-create a new one:

```bash
conda remove --name <name_of_env> --all
conda create -n <name_of_env> python=3.9
conda activate <name_of_env>
python -m pip install --upgrade pip
pip install -r requirements.txt
```
