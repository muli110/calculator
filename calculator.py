"""
Menu-Driven Calculator
Supports basic arithmetic and scientific operations.
"""

import math


def get_number(prompt="Enter number: "):
    """Prompt until the user enters a valid float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def power(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)


def sine(a):
    return math.sin(math.radians(a))


def cosine(a):
    return math.cos(math.radians(a))


def tangent(a):
    return math.tan(math.radians(a))


MENU = """
==== CALCULATOR ====
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power (a^b)
6. Square Root
7. Sine (degrees)
8. Cosine (degrees)
9. Tangent (degrees)
0. Exit
=====================
"""

# Operations needing two operands
TWO_OPERAND_OPS = {1, 2, 3, 4, 5}
# Operations needing one operand
ONE_OPERAND_OPS = {6, 7, 8, 9}


def run_calculator():
    while True:
        print(MENU)
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Please enter a valid menu number.\n")
            continue

        if choice == 0:
            print("Goodbye.")
            break

        if choice not in TWO_OPERAND_OPS and choice not in ONE_OPERAND_OPS:
            print("Invalid option. Try again.\n")
            continue

        try:
            if choice in TWO_OPERAND_OPS:
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")

                if choice == 1:
                    result = add(a, b)
                elif choice == 2:
                    result = subtract(a, b)
                elif choice == 3:
                    result = multiply(a, b)
                elif choice == 4:
                    result = divide(a, b)
                elif choice == 5:
                    result = power(a, b)

            else:  # one operand
                a = get_number("Enter number: ")

                if choice == 6:
                    result = square_root(a)
                elif choice == 7:
                    result = sine(a)
                elif choice == 8:
                    result = cosine(a)
                elif choice == 9:
                    result = tangent(a)

            print(f"\nResult: {result}\n")

        except ZeroDivisionError as e:
            print(f"\nError: {e}\n")
        except ValueError as e:
            print(f"\nError: {e}\n")


if __name__ == "__main__":
    run_calculator()