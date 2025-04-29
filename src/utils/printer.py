def print_intro():
    print("")
    print("***************************************************************\n")
    print("*** Welcome to SciCalc -- the simple scientific calculator! ***\n")
    print("***************************************************************\n")
    print("SciCalc (in a nutshell):")
    print("Give a mathematical expression and get the solution.")


def print_separator():
    print("\n" + "*" * 70)


def print_instructions():
    print("\nAllowed inputs:\n")
    print("* Numbers 0-9 (integer or floating point using the period '.' as the decimal separator)")
    print("* Constants: 'pi'")
    print("* Operators: plus '+', minus '-', multiplication '*', division '/', exponentiation '**'")
    print("* One argument functions: square root 'sqrt(x)', sine 'sin(x)', cosine 'cos(x)' "
        "(note!: When using 'sin' and 'cos', 'x' will be converted to radians, so use degrees)")
    print("* Two argument functions: minimum 'min(x, y)', maximum 'max(x, y)'")
    print("* Other characters: brackets '(', ')', and comma ',' for max and min e.g. 'min(1, 9)'")
    print("* Spaces: Use them for clarity if you want to. They will be removed in validation.")
    print("\nYou can also use capital letters A-Z as variables and set values for them.")
    print("To do this add a variable A-Z and '=' to the start of your expression")
    print("(e.g. 'A=5*5' sets 'A' to be '25').")


def print_command_options():
    print("\nCommands:\n")
    print("1: Get a solution for an expression or set a variable")
    print("2: List all defined variables")
    print("q: Quit SciCalc\n")


def print_expression_help():
    print_instructions()
    print("\n* Expressions should be written with care in proper infix notation.")
    print("* Use a period '.' as a decimal separator, not a comma ','.")
    print("* Ensure brackets are correctly paired.")
    print("* Be explicit with negative numbers and enclose them in brackets, e.g. '(-3)'. not '-3'.")
    print("* Be explicit with multiplication, e.g. '3*A', not '3A'.")
    print("\nExample expressions:")
    print("Valid: '(-2)**2*(-5.7)'")
    print("Valid: 'Z=8.55 / max(sqrt(9), 4) + pi*3'")
    print("Valid: 'Y = 3 * 4 + (-5.67) / (sin(9) + 2) * min((-5), (-2.3))'")
    print("\nNot valid: '(- 2)**a*(-5.7)' (invalid character, use capital ASCII A-Z for variables)")
    print("                   ^")
    print("Not valid: '8,5/(max(sqrt(9), -4)+pi' (should be period '.'; "
          "negative number not in brackets)")
    print("             ^                ^")
    print("Not valid: '3 / 3A + 2) / 0' (inexplicit multiplication; division with zero)")
    print("                 ^        ^")


def print_variables(user_vars: dict):
    print("\nDefined variables:\n")

    if not user_vars:
        print("You have no defined variables")
        return

    for key in sorted(user_vars.keys()):
        print(f"{key} = {user_vars[key]}")
