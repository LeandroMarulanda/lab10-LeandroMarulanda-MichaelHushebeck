# Repository: https://github.com/LeandroMarulanda/lab11-LeandroMarulanda-MichaelHushebeck/blob/main/calculator.py
# Partner 1: Leandro Marulanda
# Partner 2: Michael Hushebeck

import math

# Leandro Marulanda's functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def logarithm(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Invalid logarithm arguments")
    return math.log(a, b)

def exponent(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    if a < 0 or b < 0:
        raise ValueError("Sides cannot be negative")
    return math.hypot(a, b)


# Michael Hushebeck's functions

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def log(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Invalid logarithm arguments")
    return math.log(a, b)

def exp(a, b):
    return a ** b
