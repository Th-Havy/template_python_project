# Checklist for new projects

* [ ] Read all the sections of this documentation carefully.
* [ ] Create a new repository
    * [ ] Create a new repository on https://gitlab.ethz.ch/qudev
    * [ ] Clone this template repository
    * [ ] Follow the instructions on the README to re-initialize the Git
    repository and update its remote to the newly created GitLab repository.
* [ ] Create a virtual environment, add additional dependencies to 
`requirements.txt` (e.g `numpy`).
* [ ] Setup your IDE
    * [ ] Use the correct virtual environment.
    * [ ] Create launch/debug configurations.
    * [ ] Setup your linter.
* [ ] Add additional items in `.gitignore`, if any.
* [ ] Write a first draft of your README.
    * [ ] Summary/description of the repository
    * [ ] Cloning and installation instructions
    * [ ] Authors
* [ ] Check that you can build the documentation locally.
* [ ] Check that you can run the example tests locally.
* [ ] Remove the irrelevant documentation (i.e. the documentation of this 
template project).
* [ ] Remove the example tests.
* [ ] Make the first push to your repository.
* [ ] Agree on conventions with the other contributors:
    * [ ] Coding conventions (e.g. file, variables, functions and class naming).
    * [ ] Documentation conventions (e.g. docstring format).
    * [ ] Version control convention (e.g. git branches and code reviews).

```{note}
It is important to check that you can build the documentation and run the unit 
tests right at the beginning to be able to right either of them right from the
start.

Similarly, it is important to verify you can pull from/push to the origin of
your repository, such that you can upload your changes to thre remote web-hosted
repository (i.e GitLab). 
```