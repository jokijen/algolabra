# Testing 

Testing is implemented with unit tests (Pytest and Unittest), in addition to which the application has been manually tested. Continuous integration (CI) is implemented with a GitHub Actions (GHA) testing workflow which runs with every modification. The test coverage monitoring is handled with Codecov. 


## Unit tests 

The following classes located in the “core” directory are tested with unit tests:  

* InputValidator

To be implemented next:

* Queue
* RPNEvaluator
* ShuntingYard
* Stack

The command-line interface (ui.py) is excluded from unit testing.  


## Integration testing  

Integration testing will be implemented to ensure interactions between different components function correctly.  


## Continuous integration GitHub Actions

A continuous integration (CI) workflow for testing is implemented with GitHub Actions (GHA). The workflow tasks are defined in test.yml. First steps perform the build, after which the tests are run, a coverage report is generated, and the report is uploaded to Codecov.

The coverage report can be found on [Codecov](https://app.codecov.io/gh/jokijen/algolabra).


## Running the tests

Instructions for running the tests can be found in the document [USAGE.md](./documents/USAGE.md)