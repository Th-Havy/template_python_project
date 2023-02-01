"""File description, useful if the file contains multiple classes/functions."""


class ExampleClass:
    """Description of the class. Instance attributes are documented here.
    
    Attributes:
        x: Integer, number of something.
        y: Value of something else. You do not need to specify the type of the
            parameter if you use type hints.
    """

    SOME_VALUE = 1
    """Class attributes (not instance attributes) can be documented like so."""

    def __init__(self, x:int, y:float):
        self.x = x
        self.y = y

    def get_formatted_description(self, prefix:str="") -> str:
        """One liner description.
        
        More detailled description.
        This docstring contains the typical format that should be used when
        documenting classes and methods. Note that not all data must always be
        indicated.
        For instance, no need to indicate a detailled description if the 
        one-liner is sufficient. No need to indicate the return value, if the
        one-liner indicates it and no further information need to be conveyed.


        Arguments:
            prefix: A string prependend to the returned string.

        Raises:
            TypeError: If prefix is not a string.

        Returns:
            A string with the format `<prefix>x=<x>, y=<y>`.

        Example::
        
            from example_module import ExampleClass
            my_instance = ExampleClass(x=42, y=3.14)
            print(my_instance.get_formatted_description("values: "))
        """

        if not isinstance(prefix, str):
            raise TypeError("'prefix' should be of type 'str' instead of " \
                f"type '{type(prefix)}'.")

        return f"{prefix}x={self.x}, y={self.y}"

    def compute_y_power_x(self) -> float:
        """Ideally a clear naming (and optionally type hints) is enough to
        understand the code.
        """

        return self.y ** self.x
    
    def function_with_args_and_kwargs(self, value:int, *args, **kwargs):
        """Here is how to document a function with ``args`` and ``kwargs``.

        Args:
            value: Regular parameter.
            args (list): Positional arguments: list of additional unnamed
                arguments.
            kwargs (dict): Keyword arguments: dictionarry of additional named
                arguments. You can specify the list of accepted keyword
                arguments as follows (the immediate blank line is required for
                a correct formatting with no warnings):

                * ``x``: One option.
                * ``y``: Another option, if the description is too long to fit
                  on a single line, the new line should be aligned with the
                  start position of the first line.
                * ``z``: Last option.
        """
        pass

    class NestedClass:
        """Sphinx can't automatically extract nested classes to another file.
        
        Thus the content of the class is only shown inline in the documentation
        of the parent class.
        """
        
        NESTED = "nested class attribute"
        """An attribute of the nested class."""


class LinkAnotherClass:
    """You can also add cross-references to other functions, classes and modules.
    
    The syntax for referencing a python element is: ``:role:`title <target>```.
    The full list of roles can be found
    `here <https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#cross-referencing-python-objects>`_,
    and the ``:py`` prefix can be omitted within docstrings.
    
    For instance:

    * ``:class:`ExampleClass```, becomes a link :class:`ExampleClass`.
    * ``:meth:`ExampleClass.compute_y_power_x```, also becomes a link:
      :meth:`ExampleClass.compute_y_power_x`.
    * ``:met:`~ExampleClass.get_formatted_description```, with 
      ``~`` only the last component of the target is shown:
      :func:`~ExampleClass.get_formatted_description`
    * ``:attr:`another text <ExampleClass.NestedClass.NESTED>```, you can change
      the link to :attr:`another text <ExampleClass.NestedClass.NESTED>`.
    """


class LinkToLibraryObjects:
    """You can even cross-reference Python objects from the standard library or
    other external packages.

    Make sure you have set up the intershinx extensions, by including the
    extension (``'sphinx.ext.intersphinx'``) and specifying the libraries you 
    want to link in  ``intersphinx_mapping`` inside ``conf.py``.

    Then simply use the same syntax as described in :class:`LinkAnotherClass`.
    It is recommended to always use the fully qualified path for linking to 
    external libraries.

    For instance:

    * ``:class:`pathlib.Path```, becomes a link :class:`pathlib.Path`.
    * ``:func:`pytest.approx```, becomes a link :func:`pytest.approx`.
    """
