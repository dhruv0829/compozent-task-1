def basic_arithmetic_operations():
    # Getting input from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Performing operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else "undefined (division by zero)"

    # Displaying results
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")

basic_arithmetic_operations()
