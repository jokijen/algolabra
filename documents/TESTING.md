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
* update_user_vars: User variables are updated correctly. 
    * Inputs tested: key `A`, value `45`.
* _is_number: Identifies float and negative integer, but not functions or whole expressions
    * Inputs tested: `5.7`, `-9`, `sqrt(3)`, `3+3`
* _expand_variable: Correctly expands a variable
    * Inputs tested: var `A`with value `1.45`
* _validate_length: Does not accept an empty input
    * Inputs tested: `""`
* _validate_first_and_last: Accepts when both are valid (number, set variable, or bracket), raises an InvalidExpressionException when one is operator
    * Inputs tested: `3*32`, `A+3*32*B`, `sqrt(3)*(32+2)`, `*3+5.6`, `12*13/`
* _check_for_invalid_characters: Accepts when there are no invalid character, raises an InvalidExpressionException otherwise
    * Inputs tested: `5.65*pi+sqrt(-9)**sin(4)`
* _tokenise_expression: Correctly tokenises expression
    * Inputs tested: `12*0.6/5**(-2)+sqrt(90)-min(sin(10), 5)`
* _bracket_value: Identifies opening and closing brackets, and non-bracket characters
    * Inputs tested: `(`, `)`, `,`
* validate_expression: Accepts valid expressions (3 test cases) and identifies that the user wants to set variable. Does not accept an undefined variable or consecutive operators
    * Inputs tested: `A+(-3)*A**2.5A+(-3)*A**2.`
* _validate_tokens: Converts unary negative '-' to 'n'. Does not accept the following:
    * too many or few commas (relates to the operands given to functions min and max which contain a comma each)
        * `A+(-3)*A**2.5`, `A`, `(-A)+5+pi`, `L = (-9)**3`, `(-3)*Y**2.5`, `(-3)***2.5`, 
    * closing bracket before opening bracket or unequal brackets
        * `['min', '(','1', ',', '2', ',', '3', ')']`, `['min', '(','1', '3', ')']`, `['1', '+', ')', '1', '+', '3', '(']`, `['1', '+', '(', '-', '5', ')', '+', '3', '(']`, `['1', '+', '(', '-', '(', '3', '+', '3', ')', ')']`

##### Queue

* enqueue: Add to queue
    * Inputs tested: `[]` ->`[1, 2, 3]`
* dequeue: Remove from queue
    * Inputs tested: `[1, 2, 3]` -> `[2, 3]`
* is_empty: Returns correct boolean value for empty and nonempty queue
    * Inputs tested: `[]`, `[1]`

##### RPNEvaluator

* Operations: Addition, subtraction, multiplication, division (with nonzero and zero divisors), exponentiation, and unary negation. 
    * Inputs tested (+): `'+', 30.0, 15.5`
    * Inputs tested (-): `'-', -10.0, 10.0`
    * Inputs tested (*): `'*', 2.0, 3.6`
    * Inputs tested (/): `'/', 30.0, 2.0`, `'/', 8.0, 0.0`
    * Inputs tested (**): `'**', 20.0, 0.0`
    * Inputs tested (n): `[10.0, 2.5, 'n', '+']`
* Functions: Cosine and sine (in degrees), square root (with positive and negative radicand), min and max (with variations of min/max value first/last)
    * Inputs tested (sin/cos): `[60.0, 'cos']`, `[90.0, 'sin']`
    * Inputs tested (sqrt): `'sqrt', None, 9.0`, `'sqrt', None, -9.0`
    * Inputs tested (min/max): `-20.0, 20.0, 'min'`, `100.0, 1000.0, 'min'`, `100.0, 1000.0, 'max'`, `-20.0, 20.0, 'max'`
* A complex full expression
    * Inputs tested: `sqrt(3*3)*3**2.5+sin(51/2+25.5)-cos(51/2+25.5)/max(1+1,0)*(-1)`
* Edge cases and errors: No tokens, unrecognised token, insufficient operands for operator and functions, and overflow error. 
    * Inputs tested: `[]`, `['b']`, `'+', 1.0`, `sqrt`, `1.0, 'min`, `90000.0, 90000.0, '**'`, `1.0, 1.0, 1.0, '+'`, `-5.0, 0.005, '**'`

##### ShuntingYard

* convert_to_rpn: Converts valid token Queue to RPN format
    * Inputs tested: `[2.0, '+', '(', -2.0, ')', '*', '(', 'n', '(', 'sqrt', '(', 9.0, ')', ')', ')', '+', 'min', '(', 5.0, ',', 1.0, ')']`
* Empty input raises an InvalidExpressionException
    * Inputs tested: `[]`

##### Stack

* enqueue: Add to stack
    * Inputs tested: `[]` ->`[1, 2, 3]`
* dequeue: Remove from stack
    * Inputs tested: `[1, 2, 3]` -> `[1, 2]`
* peek: Peek a nonempty stack and peek an empty stack
    * Inputs tested: `[1, 2, 3]` -> `[3]`, `[]`
* is_empty: Returns correct boolean value for empty and nonempty stack
    * Inputs tested: `[]`, `[1]`


## End-to-end tests 

End-to-end testing is implemented with Pytest (using monkeypatch and capsys). A full user interaction with the application is tested in a realistic way, which helps verify that the application outputs are correct. 

The test cases located in `test_ui.py` contain various types of user interaction scenarios where the user's input is either valid or triggers an exception. These include evaluating exspressions and setting values for variables in varying ways. 

The following user inputs were tested: 

* test_main_with_simple_expression `["1", "1 + 2 * (-5.55)", "q"]`
* test_main_with_complex_expression `["1", "5*25/900*sqrt(9)+min(sin(60),1)", "q"]`
* test_main_view_and_set_variables `["2", "1", "A=sqrt(9)", "2", "1", "A=2**(-3)", "y", "2", "1", "A=pi", "b", "B", "2", "1", "B=6", "n", "2", "q"]`
* test_main_help `["1", "h", "c", "q"]`
* test_main_invalid_command `["r", "4", "H", "q"]`
* test_main_validation_error `["1", "min(1,2,3)", "c", "q"]`
* test_main_RPN_evaluation_error `["1", "1/0", "c", "q"]`


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
