"""This file contains examples of pytest unit tests."""

import pytest

from example_module.example_class import ExampleClass


@pytest.fixture(scope="session")
def example_class_instance() -> ExampleClass:
    """Fixture creating an initialized instance of ExampleClass.
    
    A test fixture is an environment used to consistently run tests. Typically
    one would use fixture to create and initialize objects and data prior to
    running some tests. This way there is no need for duplicated code in every
    test for getting test data.

    Test fixture can be created with the ``pytest.fixture`` decorator. Then the 
    fixtures can be accessed in subsequent tests by declaring a parameter of a
    test function with that name (e.g. ``test_get_formatted_description()``) .
    """

    return ExampleClass(42, 3.14)

def test_get_formatted_description(example_class_instance):
    """Check that the formatted string conforms with the expected format.
    
    Pytest will automatically discover the test function if they start with
    ``test_`` or end with ``_test``. Fixtures can be passed as parameters to a
    test function.
    """

    # Test without prefix
    result = example_class_instance.get_formatted_description()
    expected = f"x=42, y=3.14"

    assert result == expected

    # Test with prefix
    result = example_class_instance.get_formatted_description("values: ")
    expected = f"values: x=42, y=3.14"

    assert result == expected, "You can indicate an error message like so."

def test_get_formatted_description_exception(example_class_instance):
    """Check that a TypeError is raised when a wrong prefix type is passed.

    This is an example of test verifying that an exception is correctly raised.
    """

    with pytest.raises(TypeError):
        example_class_instance.get_formatted_description(12345678)

@pytest.mark.parametrize("x, y, expected", [
    (0, 1, 1),
    (2, 2, 4),
    (3, 3, 27),
    (0, 3.14, 1),
    (2, 2.5, 6.25),
])
def test_compute_y_power_x(x, y, expected):
    """Test the correctness of y^x.
    
    The `pytest.mark.parametrize` decorator allows to run the same test with
    multiple parameters, which can be helpful to avoid copy-pasting a lot of
    code.

    The first parameter of this decorator is a string containing parameter names
    which will be passed to the decorated function. The second argument is a
    list of tuple with the values of the parameters to be passed to the test
    function. 
    """

    instance = ExampleClass(x, y)
    result = instance.compute_y_power_x()
    assert(result == expected)