"""End-to-end tests for the application. Calls on main() in ui.py.
"""
from src.ui import main


def test_main_with_simple_expression(monkeypatch, capsys):
    user_input = iter(["1", "1 + 2 * (-5.5)", "q"])
    monkeypatch.setattr('builtins.input',lambda _: next(user_input))

    main()
    calc_output, _ = capsys.readouterr()

    assert "Validated tokens:" in calc_output
    assert "[1.0, '+', 2.0, '*', '(', -5.5, ')']" in calc_output
    assert "Reverse Polish Notation (RPN):" in calc_output
    assert "[1.0, 2.0, -5.5, '*', '+']" in calc_output
    assert "Final result:" in calc_output
    assert "-9" in calc_output
    assert "Quitting the program" in calc_output

def test_main_with_complex_expression(monkeypatch, capsys):
    user_input = iter(["1", "5*25/900*sqrt(9)+min(sin(60),1)", "q"])
    monkeypatch.setattr('builtins.input',lambda _: next(user_input))

    main()
    calc_output, _ = capsys.readouterr()

    assert "Validated tokens:" in calc_output
    assert "[5.0, '*', 25.0, '/', 900.0, '*', 'sqrt', '(', 9.0, ')', '+', 'min', '(', '(', 'sin', '(', 60.0, ')', ')', '(', 1.0, ')', ')']" in calc_output
    assert "Reverse Polish Notation (RPN):" in calc_output
    assert "[5.0, 25.0, '*', 900.0, '/', 9.0, 'sqrt', '*', 60.0, 'sin', 1.0, 'min', '+']" in calc_output
    assert "Final result:" in calc_output
    assert "1.2826920705" in calc_output
    assert "Quitting the program" in calc_output

def test_main_view_and_set_variables(monkeypatch, capsys):
    """First set A=3. Then start setting A=0.125, but it has already been defined, so uupdate A with the new value.
    Start setting A, but it has been defined so test setting b, and finally set B=.1415926536 instead.
    Start setting A=6, but cancel.
    """
    user_input = iter([
        "2", "1", "A=sqrt(9)", "2", "1", "A=2**(-3)", "y", "2", "1", "A=pi", "b", "B", "2", "1", "B=6", "n", "2", "q"
        ])
    monkeypatch.setattr('builtins.input',lambda _: next(user_input))

    main()
    calc_output, _ = capsys.readouterr()

    assert "You have no defined variables" in calc_output

    assert "Variable to set:" in calc_output
    assert "A" in calc_output
    assert "Validated tokens:" in calc_output
    assert "['sqrt', '(', 9.0, ')']" in calc_output
    assert "Reverse Polish Notation (RPN):" in calc_output
    assert "[9.0, 'sqrt']" in calc_output
    assert "Final result:" in calc_output
    assert "3" in calc_output
    assert "Variable A = 3 set!" in calc_output

    assert "A = 3" in calc_output

    assert "[2.0, '**', '(', -3.0, ')']" in calc_output
    assert "[2.0, -3.0, '**']" in calc_output
    assert "0.125" in calc_output
    assert "The variable A already has a value. Do you want to overwrite value" in calc_output
    assert "Variable A = 0.125 set!" in calc_output

    assert "A = 0.125" in calc_output

    assert "[3.141592653589793]" in calc_output
    assert "3.1415926536" in calc_output
    assert "Invalid command. Please try again." in calc_output
    assert "Variable B = 3.1415926536 set!" in calc_output
    assert "Variable A = 3.1415926536 set!" not in calc_output
    assert "B = 3.1415926536" in calc_output

    assert "[6.0]" in calc_output
    assert "6" in calc_output
    assert "The variable A already has a value. Do you want to overwrite value" in calc_output
    assert "Variable not updated" in calc_output
    assert "Variable A = 6 set!" not in calc_output
    assert "Quitting the program" in calc_output

def test_main_help(monkeypatch, capsys):
    user_input = iter(["1", "h", "c", "q"])
    monkeypatch.setattr('builtins.input',lambda _: next(user_input))

    main()
    calc_output, _ = capsys.readouterr()

    assert "Expressions should be written with care in proper infix notation." in calc_output
    assert "Quitting the program" in calc_output


def test_main_cancel(monkeypatch, capsys):
    user_input = iter(["1", "c", "q"])
    monkeypatch.setattr('builtins.input',lambda _: next(user_input))

    main()
    calc_output, _ = capsys.readouterr()

    assert "Give a mathematical expression to evaluate ('h' help, 'c' cancel):" in calc_output
    assert "Quitting the program" in calc_output

def test_main_invalid_command(monkeypatch, capsys):
    user_input = iter(["r", "q"])
    monkeypatch.setattr('builtins.input',lambda _: next(user_input))

    main()
    calc_output, _ = capsys.readouterr()

    assert "Nice try! That is not a valid command. Try again." in calc_output
    assert "Quitting the program" in calc_output

def test_main_validation_error(monkeypatch, capsys):
    user_input = iter(["1", "min(1,2,3)", "c", "q"])
    monkeypatch.setattr('builtins.input',lambda _: next(user_input))

    main()
    calc_output, _ = capsys.readouterr()

    assert "Validation error" in calc_output
    assert "Unnecessary commas!" in calc_output
    assert "Quitting the program" in calc_output

def test_main_RPN_evaluation_error(monkeypatch, capsys):
    user_input = iter(["1", "1/0", "c", "q"])
    monkeypatch.setattr('builtins.input',lambda _: next(user_input))

    main()
    calc_output, _ = capsys.readouterr()

    assert "Error when evaluating the RPN expression" in calc_output
    assert "Division with zero undefined!" in calc_output
    assert "Quitting the program" in calc_output
