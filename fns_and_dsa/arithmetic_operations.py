def perform_operation(num1, num2, operation):
    while True:
        if operation == 'add':
            return num1 + num2
        if operation == 'subtract':
            return num1 - num2
        if operation == 'multiply':
            return num1 * num2
        if operation == 'divide':
            if num2 != 0:
                return num1 / num2
            elif num2 == 0:
                print("Cannot perform operation")
            break
        
   