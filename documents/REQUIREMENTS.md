# Requirement specification

- Degree Programme: Tietojenkäsittelytieteen kandidaatti (TKT)
- Programming language: Python
- Language of documentation: English with the exception of weekly reports, which will be in Finnish
- Peer-review programming languages: Python


## Algorithms and data structures implemented

The project is an implementation of a scientific calculator that takes in a mathematical expression as user input, validates it, converts it to postfix notation, and solves it. The project uses stack and queue data structures as well as the Shunting-Yard algorithm.


## Problem statement

The user can give a mathematical expression and the application will calculate and output its value. The user may also set values for variables (capital ASCII, A-Z).


## Accepted inputs and their usage

The program receives as input a mathematical expression consisting of numbers (0–9), operators (+, -, *, /, ^), accepted characters ("(", ")", “.”, “,”) and functions (cos, sin, sqrt, max, min). The program prints the solution as an output or an informative error message if the input is invalid. The user can also set a variable. 


## Performance and time complexity

The goal is a time complexity of O(n), which is dependent on the length of the input. Different parts of the code will have time complexities O(1)-O(n) depending on the structure, e.g. stack and queue structures have a time complexity of O(1).


## Sources

- [pikuma: Shunting Yard Algorithm](https://www.youtube.com/watch?v=ceu-7gV1wd0)
- [Comp Sci in 5: Post Fix Stack Evaluator]( https://www.youtube.com/watch?v=bebqXO8H4eA)
- [Comp Sci in 5: Shunting Yard Algorithm](https://www.youtube.com/watch?v=Wz85Hiwi5MY)
- [Wikipedia: Shunting yard algorithm](https://en.wikipedia.org/wiki/Shunting_yard_algorithm)
- [Wikipedia: Reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)
