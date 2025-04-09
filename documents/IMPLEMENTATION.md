# Implementation

This document outlines the application implementation and algorithms used.

- [Application structure](#application-structure)
- [Performance and time complexity](#performance-and-time-complexity)
- [Deficiencies and improvement ideas](#deficiencies-and-improvement-ideas)
- [Use of AI tools](#use-of-ai-tools)
- [Sources](#sources)


## Application structure

The application code consists of several classes that implement different parts of the full functionality.  


### Running the app and UI

The user interface is implemented as a command-line interface. When the application is run the function “main()” is called. A dictionary for user variables is initialised. The user may interact with the application by giving commands as instructed.


### User variables

The user may view variables saved in the variables dictionary or save new variables. The variables may be individual digits or mathematical expressions.


### Solving a mathematical expression

The user may input a mathematical expression that they wish to solve. The expression must be in proper infix form (i.e. operators within the expression, such as “1 + 2”). The expression is validated and tokenised using the InputValidator and converted to Reverse Polish Notation (RPN) (i.e. operators follow the numbers/operands, such as “1 2 +”, aka postfix) with the Shunting-Yard algorithm (class: ShuntingYard). Finally, the RPN form expression is evaluated using the RPNEvaluator class, and a value returned to the user.


## Performance and time complexity

The overall time complexity is linear time O(n), which is dependent on the length of the user given input. There is some variance in time complexity between different parts of the code:

* Stack and queue operations: O(1).
* Operations on the dictionary for the user’s variables: O(1)
* InputValidator, ShuntingYard, and RPNEvaluator: O(n) where n is the length of the input

Linear time complexity O(n) is efficient in cases where it is necessary to sequentially go through the entire input. As the user provided input will not be very long (when used as intended), a more rigorous analysis would not generate any valuable information.


## Deficiencies and improvement ideas 

Currently the program is incomplete. 

### Bugs

- min/max does not function correctly when the arguments are functions. I need to add extra brackets around both arguments in the InputValidator

- sin and cos don't function correctly when the argument is in radians already (e.g. 'sin(pi)')


### Future improvement

The command-line interface is easy to use, but possibly a graphical user interface could be built with Tkinter. 


## Use of AI tools

LLMs ChatGPT-4o (Open AI) and Le Chat (Mistral AI) have been used for the following purposes: 

- Query programming best practices (especially regarding commenting)
- Assist in solving git issues and understanding programming error notifications
- Perform translations for docs I initially wrote in Finnish
- Generate versatile (valid and invalid) test inputs for development purposes


## Sources

- [pikuma: Shunting Yard Algorithm](https://www.youtube.com/watch?v=ceu-7gV1wd0)
- [Comp Sci in 5: Post Fix Stack Evaluator]( https://www.youtube.com/watch?v=bebqXO8H4eA)
- [Comp Sci in 5: Shunting Yard Algorithm](https://www.youtube.com/watch?v=Wz85Hiwi5MY)
- [Wikipedia: Shunting yard algorithm](https://en.wikipedia.org/wiki/Shunting_yard_algorithm)
- [Wikipedia: Reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)
