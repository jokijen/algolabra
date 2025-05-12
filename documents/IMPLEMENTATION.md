# Implementation

This document outlines the structure and algorithms used in the application. Additionally, it provides information on the performance and any deficiencies of the application. 

- [Application structure](#application-structure)
- [Performance and time complexity](#performance-and-time-complexity)
- [Deficiencies and improvement ideas](#deficiencies-and-improvement-ideas)
- [Use of AI tools](#use-of-ai-tools)
- [Sources](#sources)


## Application structure

The application structure is modular and classes are used for implementing different parts of the full functionality.  


### Main program and user interface

The user interface (UI) is implemented as a command-line interface (CLI). The user may interact with the application by giving commands as instructed.

The entry point is the `main()` function in `ui.py`. When run, a dictionary `USER_VARS` for user variables is also initialised. 


### Mathematical expression processing

The user may give a mathematical expression that they wish to solve as input. The expression input must be in a valid infix form (i.e. operators within the expression, such as `1 + 2 * 3`). They may use integers and floating points numbers, as well as operators (`+`, `-`, `*`, `/`, `**`) and functions (`cos`, `sin`, `sqrt`, `max`, `min`). Input validity also calls for correctly placed parentheses (e.g. to enforce precedence or enclose a negative number).

#### Pipeline 

1. The user's expression is validated and tokenised using the `InputValidator` class.

2. The Shunting-Yard algorithm (class: `ShuntingYard`) is used to convert the expression into Reverse Polish Notation (RPN) (aka postfix) where operators follow the numbers/operands (such as in the example given in the last paragraph `1 2 3 * +`). The Shunting-Yard algorithm uses a FIFO Queue and LIFO Stack for token handling. 

3. The RPN form expression is evaluated using the `RPNEvaluator`. If the expression was valid, a value is returned to the user. Otherwise the user will receive an error message outlining the issue with the input or process. 

4. If the input included variable assignment, the result is stored in the dictionary `USER_VARS` with the variable as key and result as value. 


### User variables

The user may set a variable by defining the variable they want to set (i.e. capital ASCII letter, A-Z) in their mathematical expression. Example: The mathematical expression input `A = 1 + 2` would set variable `A` to have the value `3`. The variable is set in the "Mathematical expression processing" [pipeline](#pipeline) above. 

The user may use any set variables in subsequent expressions, e.g. `3 + A * 1` if `A` has been set.

The user may also view the variables saved in the variables dictionary. 


## Performance and time complexity

The overall time complexity is linear time O(n), which is dependent on the length of the user given input. There is some variance in time complexity between different parts of the code:

* Stack and queue operations: O(1).
* Operations on the dictionary for the user’s variables: O(1)
* InputValidator, ShuntingYard, and RPNEvaluator: O(n) where n is the length of the input

Linear time complexity O(n) is efficient in cases where it is necessary to sequentially go through the entire input. As the user provided input will not be very long (when used as intended), a more rigorous analysis would not generate any valuable information.


## Deficiencies and future improvement 

The current version is functional and there are no identified bugs. Nonetheless, the application could be improved: 

* Some error messages are fairly generic and they could be made even more informative and case-specific
* The CLI is simple and could be improved visually e.g. clearer layout and use of colours. Alternatively, a GUI could be built with Tkinter.  


## Use of AI tools

LLMs ChatGPT-4o (Open AI) and Le Chat (Mistral AI) have been used for the following purposes: 

- Query programming best practices (especially regarding commenting)
- Assist in solving git issues and understanding programming error notifications
- Perform translations for docs I initially wrote in Finnish
- Generate versatile (valid and invalid) test inputs for development purposes
- Assistance with syntax when using monkeypatch for E2E-testing


## Sources

- [pikuma: Shunting Yard Algorithm](https://www.youtube.com/watch?v=ceu-7gV1wd0)
- [Comp Sci in 5: Post Fix Stack Evaluator]( https://www.youtube.com/watch?v=bebqXO8H4eA)
- [Comp Sci in 5: Shunting Yard Algorithm](https://www.youtube.com/watch?v=Wz85Hiwi5MY)
- [Wikipedia: Shunting yard algorithm](https://en.wikipedia.org/wiki/Shunting_yard_algorithm)
- [Wikipedia: Reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)
