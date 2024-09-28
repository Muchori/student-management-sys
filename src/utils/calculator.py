class Calculator:
    def add(self, a, b):
        self.validate_input(a, b)
        return a + b

    def subtract(self, a, b):
        self.validate_input(a, b)
        return a - b

    def multiply(self, a, b):
        self.validate_input(a, b)
        return a * b

    def divide(self, a, b):
        self.validate_input(a, b)
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def validate_input(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Inputs must be numbers")