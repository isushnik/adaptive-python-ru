def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a // b

operations = {"plus": plus, "minus": minus, "multiply": multiply, "divide": divide}

a, operation, b = input().split()
print(operations[operation](int(a), int(b)))
