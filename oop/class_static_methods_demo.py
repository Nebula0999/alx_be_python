# class_static_methods_demo.py

class Calculator:
    # Class attribute shared by all instances
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method to return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method that prints the calculation type and returns the product."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
