# exceptions.py

class CalculatorError(Exception):
    pass

class EmptyListError(CalculatorError):
    pass

class DivisionByZeroError(CalculatorError):
    pass