# Writing unit tests with Pytest

Software testing is an essential part of the developmnent process. Please refer
to the Qudev testing guidelines (**TODO: add link**) for the motivation and best
practices for testing your sofware projects. This document will thus focus more
on *how* to test your code with Pytest rather than *why*.

## Pytest

[Pytest](https://docs.pytest.org) is a very popular Python testing package. This
is the testing package included with this template repository.

If you wish to install it for another project, simply run `pip install pytest`
(in your Python virtual environment).

Pytest allows to quickly implement tests, and also provides flexibility for
covering more test cases. Here is a non-exhaustive list of Pytest's features:
* Simple syntax, possibility to use standard assertions.
* Automatic tests discovery, if you follow naming conventions.
* Command-line interface, good integration in IDEs (in particular VS Code).
* Parametrized tests.
* Test Fixtures.
* Compatible with the `unittest` standard Python library.

(running_the_tests)=
## Running the tests

Running all existing tests is really straightforward, simply run the following
command:

```bash
# Make sure to have activate your virtual environment
# This assumes that the tests are placed in a folder called 'tests'
python -m pytest tests
```

For instance, running the tests of this template repository will output:
```
============================= test session starts ==============================
collected 7 items

tests\test_example_module.py .......                                      [100%]

============================== 7 passed in 0.05s ===============================
```

If you have a lot of tests in your project, running all of them may take several
minutes. You can run only a subset of all tests by specifying a folder, file or
test function to run:

```bash
# Run tests from a specific folder
python -m pytest tests/<path/to/some/test/folder/>
# Run tests from a specific file
python -m pytest tests/<path/to/some/test_file.py>
# Run a specific test function
python -m pytest tests/<path/to/some/test_file.py>::<name_of_test_function>
```


## Writing tests

(structure_of_the_tests)=
## Structure of the tests

Your tests should be well separated from your regular code. To this end, we
recommend creating a `tests` folder at the root of your repository, and to place
all your test files and data there.

Similarly to your code and documentation, the `tests` folder should be
adequately structured with subfolders. The tests should be organized logically
or grouped thematically. You can also mirror the structure of the codebase you
test, if there are a lot of files to test. Agree on a folder structure and 
conventions with the other contributors and stick to it.

When running tests (as explained in [this section](running_the_tests)), Pytest
will automatically discover and run test files and functions if they follow some
[conventions](https://docs.pytest.org/en/6.2.x/goodpractices.html#conventions-for-python-test-discovery):
* Python files prefixed with `test_` or suffixed with `_test` will be executed.
* Within these files, your test functions should be prefixed with `test`.
* Pytest will recursively inspect the folders to find all the tests, unless a
specific test module, file or class is specified.

## Example of unit tests

You can have a look at the file
[tests/test_example_modules.py](included_source_files/test_example_module) for
some examples of how to write unit tests with Pytest. We will now give some 
explanations on specific use cases.

### Simple test as a function

The easiest way to write a test is to create a regular python function in a test
file, following the conventions as specified [earlier](structure_of_the_tests).

Within this function, you will run the part of the code you want to test, and
write assertion statements to check the output/outcome of the code. Here is an
example:

```python
def test_1_plus_1_equals_2():
    """You can write a description of the test in the docstring, if the function
    name is not explicit enough."""

    assert 1 + 1 == 2
```

If you run this test you will obtain the following output:
```
collected 1 item

tests\test.py .                                                           [100%]
============================== 1 passed in 0.01s =============================== 
```


You can also write more than one assertion per test. In that case you can also
indicate a custom error message, such that if the assertion is verified, the
output will be clearer.

```python
def test_with_errors():
    assert 1 + 1 == 2, "This test will pass."

    odd_number = 3
    assert odd_number % 2 == 0, f"Number {odd_number} is not even."
```

Running the previous test will yield:
```
collected 1 item

tests\test.py F                                                           [100%]

=================================== FAILURES ===================================
_______________________________ test_with_errors _______________________________

    def test_with_errors():
        assert 1 + 1 == 2, "This test will pass."

        odd_number = 3
>       assert odd_number % 2 == 0, f"Number {odd_number} is not even."
E       AssertionError: Number 3 is not even.
E       assert (3 % 2) == 0

tests\test.py:5: AssertionError
============================ short test summary info ===========================
FAILED tests/test.py::test_with_errors - AssertionError: Number 3 is not even.
=============================== 1 failed in 0.01s ==============================
```

Pytest will always report the tests that failed (assertion raised) or caused an
error (Uncaught exception within a test). The output message will include all
the information to locate the failed tests (name, file, line) and the context
in which the test failed. This is extremely helpful to locate the source of an
error and fix it.

### Parametrized tests

Oftentimes, the same test should be run with different parameters to account
for various scenarios, range of values or corner cases. In this case, it may be
convenient to write a parametrized test, to which multiple input values will be
passed. This way the structure of the test will remain the same for all test
cases, preventing potential copy-paste errors.

In Pytest, this can be done with the `pytest.mark.parametrize` decorator (link
to [documentation](https://docs.pytest.org/en/6.2.x/parametrize.html)). Let's
look at an example:

```python
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 1),
    (4, 2, 2),
    (2, 4, 0.5),
    (0, 1, 0),
    (1, 0, float('nan')),
])
def test_division(a, b, expected):
    assert a / b == expected
```

The first parameter of the decorator is a string containing comma-separated 
names of parameters which will be passed to the decorated function 
(`test_division()`). The second parameter is a list of tuples, where each tuple
should contain the values of the parameters specified in the first parameter.

When running the test, Pytest will run the function several times with the
specified value tuples. It will report the success/failure of each case, so as
to identify directly which combination of parameters fails.

Running the example test would yield the following output:

```
collected 5 items

tests\test_example_module.py ....F                                        [100%]

=================================== FAILURES ===================================
____________________________ test_division[1-0-nan] ____________________________

a = 1, b = 0, expected = nan

    @pytest.mark.parametrize("a, b, expected", [
        (1, 1, 1),
        (4, 2, 2),
        (2, 4, 0.5),
        (0, 1, 0),
        (1, 0, float('nan')),
    ])
    def test_division(a, b, expected):
>       assert a / b == expected
E       ZeroDivisionError: division by zero

tests\test_example_module.py:16: ZeroDivisionError
=========================== short test summary info ============================
FAILED tests/test_example_module.py::test_division[1-0-nan] - ZeroDivision...
========================= 1 failed, 4 passed in 0.10s ==========================
```

As you can see on the second-to-last line, the culprit is that dividing by 0
raises an Exception instead of the expected value. The input values are 
indicated in `FAILED tests/test_example_module.py::test_division[1-0-nan]`, 
inside the brackets.

### Test that functions raise an exception

If your function should raise exceptions in certain scenarios, you should use a
special idiom to test this with Pytest, as shown in the following example:

```python
def test_exception_raised():
    with pytest.raises(ZeroDivision):
        # This will trigger a ZeroDivision error
        a = 2 / 0
```

Such a test will pass only if the specific error/exception type is raised inside
the with statement. If the exception is not raised, the test will fail and an
error message of the form `Failed: DID NOT RAISE <class 'TypeError'>` will be
displayed in the test report.

### Test fixtures

When running unit tests, you often need to initialize and bring the class
instances you want to test to a determined state. For instance if the class you
test interacts with a database, you will need to create a test database and fill
it with some data before you can run your tests. 

Creating this test data, or reaching the state you want to test, will probably
need to be done for multiple tests. In order to limit duplicate code, and to
reduce the run time of the tests, it is useful to have a convenient way to 
access such pre-initialized python objects, which are refered to as *fixtures*.

Pytest provides powerful features for creating and using test fixtures, please
refer to the [documentation](https://docs.pytest.org/en/6.2.x/fixture.html).

Creating a 

```python
@pytest.fixture(scope="session")
def opened() -> ExampleClass:

    return ExampleClass(42, 3.14)
```