# Version control with Git

You should track and manage changes made to your source code using Git.
Please refer to the Qudev version control guidelines (**TODO: add link**) for
the motivation and best practices for version control of your projects. This
document will thus focus more on *how* to use Git for version control of your
project rather than *why*.

Git(https://git-scm.com/) is a de-facto standard version control tool. It allows
you to efficiently track all changes made to your codebase, and provides
advanced branching/merging features.

Git is useful not only to have access to all the history of modifications of
your code, but also critical when you are working with multiple people on the
same files.

The benefits of using Git are really worth the effort that you need to invest to
learn it. You can use the provided [references](git_references) to learn more
about Git.

## Installation

If you use Linux or Mac, git is already installed on your computer and ready to
be used. On Windows, you need to install
[Git for Windows](https://git-scm.com/download/win).

## Command line or GUI

Git is primarly a command-line interface tool, used in a terminal. On Linux/Mac
you can run git directly in any terminal. On windows, you can use `Git Bash` if
you installed Git for Windows.

Only a few commands are use daily, so we would recommend you to get familiar
with the following commands (refer to the 
[Git Cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf)):
* `git init`
* `git clone`
* `git add`
* `git commit`
* `git push`
* `git pull`
* `git branch`
* `git checkout`
* `git merge`

If you prefer to use a GUI instead of the command line, there are several 
options available such as `Git GUI` (bundled with `Git for Windows`), GitKraken,
and more. You can have a look at this
[list of Git GUI clients](https://git-scm.com/downloads/guis) Most IDEs also
have extensions to integrate with Git, such that Git can be used directly into
the IDE. [Visual Studio Code](https://code.visualstudio.com/) is a good IDE
which comes directly with integrated Git tools.

In the end, choose whichever tool you are more comfortable with. GUI are great
for visualizing the commit or branch history, and we would recommend to learn
how to use Git from the command line, as you might to use it for more complex
scenarios.

## The importance of conventions

Git is a very powerful tool, which provides fast and efficient version control
features. However, it is but a tool, and you need to decide how you want to use
it.

It is important to discuss with your team, and establish conventions and
guidelines on how to use Git. In particular, the following aspects you be
carefully discussed:
* **Commit messages**: What format and what should they contain?
* **Branching strategy**: What is the strategy to incorporate the changes from
different branches.
* **Branch naming**: Establish a convention for the naming of branches. For
instance, you can use these rules:
    * `master`: Principal branch, into which all changes should eventually be
    integrated. It should be a stable branch, where the code is always in a good
    state (e.g. it can at least run).
    * `feature/<feature_name>`: For implementing new features.
    * `fix/<bug_identifier>`: For fixing bugs and issues.
    * `doc/<modification>`: Modification only of the documentation.
* **Merge/Pull requests**: When should branches be merged, and what is the
process to follow. We recommend opening Merge requests on GitLab, so that
feedback can be provided, and a discussion can be recorded on the changes that
need to be made before merging the branch. 
* **Code reviews**: When and how should the code be reviewed. A Merge request is
a good time to give feedback on the code, its architecture, and points of 
improvement. 

## Ignoring files

When working with Git, it is important to commit only relevant files to your
repository. In particular, you should not commit large data files (e.g. output
from your code, experiment measurements, generated images, logs, etc.). There
are two main reasons for this:
* The data does not need to be version controlled.
* Your repository will be too large (and thus slower to clone) if you include
irrelevant large files.

Git provides a mechanism with a hidden `.gitignore` file at the root of the
repository in which one can specify files to ignore, such that they are simply
not considered by Git,  suppressing the risk of accidentally committing unwanted
files.

In this file, you can simply list folder and files to be ignored. You can also
specify rules to exclude files which have a specific naming scheme, or to
exclude all files of a given type.

You can learn more about the `.gitignore` file
[here](https://www.atlassian.com/git/tutorials/saving-changes/gitignore).


(git_references)=
## References

You can use the following references to learn more about Git, and the features
it offers.

* [Git Cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf) 
* [1h introduction video](https://www.youtube.com/watch?v=8JJ101D3knE)
* [Pro Git book](https://link.springer.com/content/pdf/10.1007%2F978-1-4842-0076-6.pdf)
