# Using SciCalc on the command-line

SciCalc is a simple scientific calculator program with a command-line interface. This document contains instructions on how to set up and run it on Linux. 


## Set up and use

Follow these steps to set up and use the application. 

1. Clone the repository with:
```
git clone https://github.com/jokijen/algolabra.git
```
2. Go to the root directory:
```
cd algolabra
```
3. Ensure you have poetry installed and if not, [install poetry](https://python-poetry.org/docs/). 
4. Install the project in one of two ways:
- Install as a package (recommended). Installs the project as a reusable Python package, which makes it available for import and use by other Python scripts and applications. 
```
poetry install
```
- Install dependencies only. Installs only the dependencies specified in the pyproject.toml file, without installing the project as a package.
```
poetry install --no-root
```
5. Activate the virtual environment with:
```
poetry shell
```
6. Start the application with:
```
python3 src/index.py
```
7. Use the application according to the instructions given. Select commands from the given options and give input where prompted to do so.
```
Commands:
1: Get a solution for an expression
2: List all defined variables
q: Quit SciCalc
```
8. To quit the application give the command "q" when prompted or use *ctrl + c*.
9. Exit poetry shell with:
```
exit
```


## Run tests and generate a coverage report

After setting up the application using the above instructions, you can run tests and generate a coverage report with the instructions found in [TESTING.md](TESTING.md#running-the-tests).
