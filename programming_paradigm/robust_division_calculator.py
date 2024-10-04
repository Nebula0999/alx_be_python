# robust_division_calculator.py
def safe_divide(numerator, denominator):

    try:
        # Convert input values to floats
        num = float(numerator)
        denom = float(denominator)

        # Perform division and check for division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."
        
        result = num / denom
        return f"The result of the division is {result:.1f}"

    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."

    
        
