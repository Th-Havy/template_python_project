# Visual studio Code setup

Visual Studio Code is a code editor developped by Microsoft available on
Windows, Linux and macOS. It has a large community and good support. It is a
great IDE that supports many programming languages, and is a good choice for
Python development.

Here is a non-exhaustive list of its features:
* Syntax highlighting
* Code completion
* Git integration
* Debugging 
* Rich list of extensions 

## Installation

The installation is really straightforward. Head over to the
[official website](https://code.visualstudio.com/) and download the latest
version for your OS.

One of the powerful feature of VS Code is its rich collection of extensions. You
can access the extension panel with `Ctrl+Shift+X`. We recommand the following
extensions:
* `Python`: to be able to execute, debug and browse Python code effectively.
* `Git Graph`: a nice extensions for visualizing the commit and branching
history of your Git repository (see Figure {numref}`git_graph`).

(git_graph)=
```{figure} images/git_graph.png
:align: center

Git Graph extension
```

Extensions can be created by anyone, so do not blindly install any extension.
You can safely install any extension created by Microsoft, which are usually
very good. You can use the number of download and the grade of the extension to
have an idea of its quality.

## Customizing your workspace

VS Code is highly customizable, and you can access the settings in the top menu
`File > Preferences > Settings`. Do not be overwhelmed by the number of
settings, you can use the search bar to find a specific one.

One settings that you should set is to enable a vertical ruler in the code
editor, which is useful if your coding conventions enforce a maximum line
length policy. Search for `rulers` in the settings to add one. You might need to
click on a button `Edit in settings.json`, in which case you can add the
following code to add a vertical ruler:

```js
"editor.rulers": [
    80, // This is the character limit for the ruler
],
```

Your IDE settings are personal and should be customized to your liking. This is
why, it is recommanded not to commit any IDE specific files (e.g. `.vscode`
folder) to your Git repository. Make sure to properly setup rules in your
`.gitignore` file to exclude irrelevant IDE configuration files. This template
repository is already setup to ignore all VS Code-specific files.

(selecting_a_virtual_env)=
## Selecting a virtual environment

If you have installed the Python extension for VS Code, you should be able to
select a specific virtual environment that VS Code will use when you run your
code, to fetch autocompletion information, etc.

To change the virtual environment that you use, press `Ctrl+Shift+P` and type
`Python: Select Interpreter`. You can then select the correct Python version to
use from the list (see Figure {numref}`select_interpreter`). If you have
Anaconda installed on your PC, VS Code is able to list the available conda envs;
it is also able to detect a local folder with a `venv` virtual environment.

(select_interpreter)=
```{figure} images/select_interpreter.png
:align: center

`Ctrl+Shift+P` : `Python: Select Interpreter`
```

## Linter setup

A linter is a static code analysis tool that inspects your code without running
it used to flag programming errors, bugs, stylistic errors and suspicious
constructs. Using a linter is an easy way to improve your code quality and
reduce the risk of missing trivial errors.

There are several linters available for Python, and we recommend
[Pylint](https://pylint.org/), which comes already setup with this template
repository.

Pylint is by default supported in the VS Code Python extension, so it is very
easy to configure it. Make sure to have already created a Python virtual
environment, and that you have installed pylint inside it
(`pip install pylint`). Then in VS Code do the following:
1. `Ctrl+Shift+P`, type `Python: Enable/Disable Linting`, and enable it.
2. `Ctrl+Shift+P`, type `Python: Select Linter`, and select `pylint`.

You should now get additional information when looking at some code, as shown in
Figure {numref}`linter`

(linter)=
```{figure} images/linter.png
:align: center

Example of linting suggestion
```

## Creating launch configurations

You can run and debug your code directly inside VS Code. In order for the code
to run properly, you must first set up some launch targets.

Go to the Run and Debug panel (`Ctrl+Shift+D`), and click
`create a launch.json file` > `Python` > `Python file`.

Here is a typical `launch.json` which you can copy for your project:

```js
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "env": {
                "PYTHONPATH": "${workspaceFolder}",
                "CONDA_DLL_SEARCH_MODIFICATION_ENABLE": "1",
            },
        },
    ]
}
```

## Git integration in VS Code

VS Code comes with Git support by default. If you open a repository
(`File > Open Folder`), VS Code will detect the hidden `.git` folder and will
then be able to show you additional change information.

### Inspecting changes

You can open up the source control panel by pressing `Ctrl+Shift+G`. In this
panel you can inspect which files where modified since the last commit. Clicking
on one of the modified files will open a *diff view*, where you can easily check
what modifications where made (see Figure {numref}`vs_code_diff`).

(vs_code_diff)=
```{figure} images/vs_code_diff.png
:align: center

Diff view in VS Code
```

Similarly, VS Code will indicate the lines that have been modified since the
last commit for any opened file which is tracked by Git. A line of color next
to the line number indicates if the line was added (green), modified (blue) or
if lines were deleted (red), as shown in Figure {numref}`inline_diff`.

(inline_diff)=
```{figure} images/inline_diff.png
:align: center

Line diff hints in VS Code
```

If you have installed the `Git Graph` extension (Figure {numref}`git_graph`),
you can bring up the history of commits and branches, by clicking the button
shown in Figure {numref}`git_graph_button`.

(git_graph_button)=
```{figure} images/git_graph_button.png
:align: center

Button to open a `Git Graph` window
```

### Running Git commands in VS Code GUI instead of the command line

If you are not confortable with using Git on the command line, you can do most
of the Git operation in VS Code. If you want to commit files from VS Code, you
must first stage your changes (corresponds to `git add <file>`), as shown in 
Figure {numref}`stage_change`.

(stage_change)=
```{figure} images/stage_change.png
:align: center

`git add` graphically in VS Code
```

You can then commit the changes by clicking the `...` button in the source
control panel, and choosing `Commit > Commit Staged`, as shown in Figure
{numref}`commit_change`

(commit_change)=
```{figure} images/commit_change.png
:align: center

`git commit` graphically in VS Code
```

You can run a lot more commands graphically by clicking the `...` button in the
source control panel, and selecting the appropriate command. In particular, you
can pull from/push to a remote.

## Pytest integration in VS Code

VS Code can be configured to work with different unit testing frameworks. Its
integration with Pytest is in particular very good. Tests can be ran and
debugged directly inside VS Code, and you can graphically see which tests are
passing or failing.

### Configuration

To configure VS Code to be able to work with Pytest, you must first make sure
to have created a virtual environment in which the `pytest` package is
installed. Make sure to have selected the proper virtual environment in VS Code
(see [this section](selecting_a_virtual_env)).

Bring the command palette `Ctrl+Shift+P`, and type `Python: Configure Tests`,
select `pytest` in the list, then select the directory containing your tests
(e.g `tests`).

### Running and debugging tests inside VS Code

After having configured pytest, you can go over to the Testing panel (Figure
{numref}`testing_panel`).

(testing_panel)=
```{figure} images/testing_panel.png
:align: center

Testing panel in VS Code
```

Here is a summary of how to use it:
1. Open the testing panel.
2. Discover the list of tests.
3. Run all tests.
4. Run an individual test.