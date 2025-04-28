# Using SciCalc on the command-line

SciCalc is a simple scientific calculator program with a command-line interface. This document contains instructions on how to set up and run it on Linux. 


## Set up and use

Follow these steps to set up and use the application: 

1. Clone the repository with
```
git clone https://github.com/jokijen/algolabra.git
```
2. Go to the root directory
3. Ensure you have poetry installed. If not, [install poetry](https://python-poetry.org/docs/) 
4. Install dependencies with:
```
poetry install
```
5. Activate the virtual environment with:
```
poetry shell
```
6. Start the application with:
```
python3 src/index.py
```
7. Use the application according to the instructions given. Select commands from the given options and give input where prompted to do so
```
Commands:
1: Get a solution for an expression
2: List all defined variables
q: Quit SciCalc
```
8. To quit the application give the command "q" when prompted or use *ctrl + c* 
9. Exit poetry shell with:
```
exit
```


## Run tests

After setting up the application using the above instructions, you can run tests with: 
```
poetry pytest
```