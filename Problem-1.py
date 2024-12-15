class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return a / b
    def calculate(self, operation, a, b):
        if operation not in ['+', '-', '*', '/']:
            raise ValueError("Invalid operation. Please use '+', '-', '*', or '/'.")
        if operation == '+':
            return self.add(a, b)
        elif operation == '-':
            return self.subtract(a, b)
        elif operation == '*':
            return self.multiply(a, b)
        elif operation == '/':
            return self.divide(a, b)

    def __init__(self):
        pass
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
operation = input("Enter the type of operation (+, -, *, /): ")

calci = Calculator()
try:
    result = calci.calculate(operation, a, b)
    print(f"The result of {a} {operation} {b} is: {result}")
except Exception as e:
    print(f"Error: {e}")
