import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def square(a):
    return a ** 2

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def log(a):
    if a <= 0:
        raise ValueError("Cannot take log of zero or negative value")
    return math.log(a)

def sin(a):
    return math.sin(math.radians(a))

def cos(a):
    return math.cos(math.radians(a))

def percentage(a, b):
    # Returns a percent of b
    return (a / 100) * b
