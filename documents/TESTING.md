# Testing 

Testing is implemented with unit tests (Pytest, Unittest) and end-to-end tests (Pytest). In addition, the application has been manually tested. 

Continuous integration (CI) is implemented with a GitHub Actions (GHA) testing workflow which runs with every modification. The test coverage monitoring is handled with Codecov. 


## Unit tests 

The following classes located in the `core` directory are tested with unit tests:  

* InputValidator
* Queue
* RPNEvaluator
* ShuntingYard
* Stack

The command-line interface `ui.py` is excluded from unit testing.  


### Test coverage

The up-to-date coverage status can be found in [README.md](../README.md).

The test coverage graph can be found below. The inner circle is the `core` directory, and outside of it are the single files in it. The colour and size of a slice represents the coverage status (with green=high, red=low) and number of statements, respectively.

![Coverage graph](https://codecov.io/gh/jokijen/algolabra/graphs/sunburst.svg?token=2GTNJF0H46)


### Test cases

##### InputValidator

* Constructor sets up the user variable dictionary correctly
* update_user_vars: User variables are updated correctly
* _is_number: Identifies float and negative integer, but not functions or whole expressions
* _expand_variable: Correctly expands a variable
* _validate_length: Does not accept an empty input
* _validate_first_and_last: Accepts when both are valid (number, set variable, or bracket), raises an InvalidExpressionException when one is operator
* _check_for_invalid_characters: Accepts when there are no invalid character, raises an InvalidExpressionException otherwise
* _tokenise_expression: Correctly tokenises expression
* _bracket_value: Identifies opening and closing brackets, and non-bracket characters
* validate_expression: Accepts valid expressions (3 test cases) and identifies that the user wants to set variable. Does not accept an undefined variable or consecutive operators
* _validate_tokens: Converts unary negative '-' to 'n'. Does not accept the following:
    * too many or few commas (relates to the operands given to functions min and max which contain a comma each) 
    * closing bracket before opening bracket or unequal brackets

##### Queue

* enqueue: Add to queue
* dequeue: Remove from queue
* is_empty: Returns correct boolean value for empty and nonempty queue

##### RPNEvaluator

* Operations: Addition, subtraction, multiplication, division (with nonzero and zero divisors), exponentiation, and unary negation. 
* Functions: Cosine and sine (in degrees), square root (with positive and negative radicand), min and max (with variations of min/max value first/last)
* Edge cases and errors: No tokens, unrecognised token, insufficient operands for operator and functions, and overflow error. 

##### ShuntingYard

* convert_to_rpn: Converts valid token Queue to RPN format
* Empty input raises an InvalidExpressionException

##### Stack

* enqueue: Add to stack
* dequeue: Remove from stack
* peek: Peek a nonempty stack and peek an empty stack
* is_empty: Returns correct boolean value for empty and nonempty stack


## End-to-end tests 

End-to-end testing is implemented with Pytest (using monkeypatch and capsys). A full user interaction with the application is tested in a realistic way, which helps verify that the application outputs are correct. 

The test cases located in `test_ui.py` contain various types of user interaction scenarios where the user's input is either valid or triggers an exception. These include evaluating exspressions and setting values for variables in varying ways. 


## Continuous integration GitHub Actions

A continuous integration (CI) workflow for testing is implemented with GitHub Actions (GHA). The workflow tasks are defined in `test.yml`. First steps perform the build, after which the tests are run, a coverage report is generated, and the report is uploaded to Codecov.

The coverage report can be found on [Codecov](https://app.codecov.io/gh/jokijen/algolabra).


## Running the tests

After setting up the application with the instructions found in [USAGE.md](USAGE.md), you can run the tests with: 
```
poetry pytest
```


## Generating a coverage report

After setting up the application with the instructions found in [USAGE.md](USAGE.md), you can generate a coverage report titled `index.html` to the `htmlcov` directory by running: 
```
coverage run --branch -m pytest
coverage report -m
coverage html
```
