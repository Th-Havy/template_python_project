# Writing documentation with Sphinx

The documentation of your codebase is as important as the code itself.
Please refer to the Qudev documentation guidelines (**TODO: add link**) for the
motivation and best practices for documenting your projects. This document will
thus focus more on *how* to document your project rather than *why*.

The recommended tool at Qudev for writting documentation for your Python
projects is **Sphinx**.

Sphinx is a powerful tool for creating Python documentation. Here is a 
non-exhaustive list of its features:
* Multiple output format: static HTML, LaTeX and PDF.
* Automatic parsing of Python docstring.
* Cross references: pages, but also Python function and classes.
* Searchable: Doc pages can be searched to quickly retrieve information.
* Extensible: Lots of extensions available.

## Initial setup of Sphinx

```{note}
If you create your repository based on this one, you can skip this sub-section,
as the Sphinx documentation is already setup. However, this sub-section can be 
interesting for your understanding, or if you would like to set Sphinx up from
scratch.
```

Setting up Sphinx requires a Python virtual environment with the following
packages: 

```bash
# Make sure your virtual environment is activated (conda activate name_of_env)
pip install sphinx sphinx-rtd-theme myst-parser
```

It is recommended to create a `docs` folder, such as to keep the repository
structure tidy:
```bash
# In the root of your repository
mkdir docs
cd docs
```

Then you can use Sphinx utility that sets up a source directory and creates a
default configuration file:
```bash
sphinx-quickstart
```

The script will ask for a few information:
* `Separate source and build directories?`: yes (enter `y`)
* `Project name`: Indicate the name of your project.
* `Author name(s)`: List of authors
* `Project release`: Version (e.g. `1.0`), can be left empty
* `Project language`: Leave empty or type `en`.

Using these options, your `docs` folder should now look like this:
```
|-- docs 
    |-- build # Output will be placed here, git-ignore this folder
    |-- source # Place your documentation in there
        |-- _static # Put .css files in there, it will most likely remain empty
        |-- _template # Templates for format of generated pages
        |-- conf.py # Sphinx configuration file
        |-- index.rst # File defining the index page of your documentation
```

You then need to modify `conf.py` and `index.rst` to finalize the setup. Look
at `conf.py` in this repository or at the 
[Sphinx documentation](https://www.sphinx-doc.org/en/master/contents.html) for
reference.

## Building the documentation

Building the documentation is straightforward:

```bash
# From root of repository
cd docs
make html
```

The documentation can then be browsed by opening `docs/build/html/index.html`.

## Writing documentation

Your documentation comes from two places:
* Documentation files: Text-based files in which you write information related
to the project, such as a user manual. You can choose to write these files
either in Markdown (`.md`), or in ReStructuredText (`.rst`).
* Inline documentation: Docstrings in your Python files. Sphinx will execute
the Python files you specify to extract the docstrings.

### Structure of the documentation

Your documentation files shouldbe placed in `docs/source` (or one of its 
subfolder). Make sure to have a clear structure for your documentation, and
organize your documentation files in sub-folders accordingly.

Make sure to include the files you write in `index.rst` which is the entry point
of your documentation.

### Writing files in ReStructuredText

Files can be written in ReStructuredText, which is the official language
supported by Sphinx. Please refer to the
[documentation](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
for the basic syntax of the language.

ReStructuredText is a powerful language which provides advanced features and
extensibility. However, this extra power comes at the price that it is not so
easy to learn. Additionally, its syntax relies on tabs, which is cumbersome.

We recommend writting only the index page in ReStructuredText, as it needs to 
use  extensively the features of the language (e.g. to generate the table of 
contents).

The rest of the documentation can be written in Markdown, as described in the 
next sub-section.

### Writting files in Markdown

Using the `myst-parser` Sphinx extension, documentation files can be written in
Markdown. The syntax of this language is much simpler than ReStructuredText and
is meant to be highly readable both as raw text and in a formatted version.

Markdown is typically used for written the top-level `README.md` of a repository
and its syntax is simple enough to focus on the content of the documentation
rather than its form.

Here is a link to a good summary of the
[Markdown syntax and features](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf).

Within the documentation files you can use additional Sphinx features provided
by the `myst-parser` extension. Please refer to the
[documentation](https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html#) 
for the full list of additional features.

A few relevant features are described below.

#### Numbered figure with caption

Snippet:

````md
(label_to_reference_the_image)=
```{figure} images/adding_image.png
:align: center

The caption under the image
```
````

Result:
(adding_image)=
```{figure} images/adding_image.png
:align: center

The caption under the image
```

The figure number of the image can be referenced, e.g. Figure 
{numref}`adding_image` as follows:

```md
A reference to Figure {numref}`label_to_reference_the_image`
```

#### Adding a note/warning

The syntax is the following (change `note` to `warning` for a warning box):
````md
```{note}
Some note in a box
```
````

This would result in the following:

```{note}
Some note in a box
```
```{warning}
Some warning in a box
```

### Writting Python docstrings

Docstring are a powerful tool for inline documentation of your Python code. They
allow you to document files, classes function and constants or variables.

Docstrings are placed directly after the element to document, and are created
as follows:

```python
class MyClass
"""Here is a docstring describing MyClass."""
    pass
```

There is no restriction on the content of a docstring, but it is recommended to
follow a common formatting, such that all the documentation is homogenous within
the whole project. Establish a documentation format for your docstring right at
the start of a project, so that all contributors know how to write their
docstrings.

A docstring usually contains the following elements:
* A one-liner summary.
* A detailed description.
* A description of arguments for functions, or of attributes for classes.
* A description of the return value for functions.
* A list of raised errors/exceptions.

Using a consistant format for docstrings also facilitates the automatic 
extraction of docstring. Sphinx has powerful features for autogenerating 
documentation for Python code based on the docstring. We recommend using
[Google's docstring formatting](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).
You can also look at the file 
[example_module/example_class.py](included_source_files/example_class.rst) in
this repository to see how you can document the various elements of your code.

Docstrings are not only important for documentation, they can also be of great
help when coding. Indeed, your IDE will typically extract the docstrings when
parsing your files, and provide contextual help when you type code or hover
above a class or function name.

### Python type hints

Type hinting is a feature introduced in `Python 3.5`. It is a syntax for 
annotating the type of variables or parameters in the code. Here is an example
of type hints:

```python
# Variable annotation
my_var:int = 123

# Function annotation
def my_function(a:str, b:str) -> str:
    return f"{a}{b}"
```

As the name implies, type hints are nothing but *hints*. They provide help for
libraries or tools (linter, IDE, etc.) but Python does not enforce any type
checking when hints are indicated. For instance the following line can be
executed with no error (although writting such a hint is pure madness!):

```python
# Misleading annotation
my_var:int = "abc"
```

Type hints can be really helpful to give context to people reading your code, as
they will know which types are expected in your functions. This is why it is 
recommended to use type hints for your high-level APIs, if they are to be used
by others.

Please note that Sphinx will also extract the type of your class/functions
arguments if you add type hints to them.

Annotations can also be helpful while typing code; if you set up your IDE
correctly, you will get more relevant code completion, as your IDE will parse
the hints to determine the type of variables. If you have a linter set up, it
will also provide you with more helpful warnings/errors if it can get additional
context from the type hints.

A final word of caution: do not abuse type hints. You can create very convoluted
annotations such as `a:Union[Tuple[List[Union[int, str]], Optional[str]]]`, but
the hints are of no use if it takes people 5 mins to understand them.

```{note}
The official documentation for type hints can be accessed
[here](https://docs.python.org/3/library/typing.html). A good summary of the
possible annotations can be found
[here](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html).
```

### Auto-generated documentation from dosctrings and hints

Here is a code snippet to add in `index.rst` to recursively auto-document a
Python module and all of its submodules:

```rst
.. autosummary::
   :toctree: _autosummary
   :template: recursive_module.rst
   :recursive:

   example_module
```

```{note}
The documentation for autogenerating Python documentation with Sphinx can be
found [here](https://www.sphinx-doc.org/en/master/usage/quickstart.html#autodoc).
```