num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case operation:
        if operation == "+":
            print(f"The result is {num1 + num2}.")
        if operation == "-":
            print(f"The result is {num1 - num2}.")
        if operation == "*":
            print(f"The result is {num1 * num2}.")
        if operation == "/":
            while num2 != 0:
                print(f"The result is {num1 / num2}.")
                break
            if num2 == 0:
                print("Cannot perform division")