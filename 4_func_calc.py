import math

# Adds two numbers
def add(num1, num2):
    return num1 + num2
# Subtracts two numbers
def subtract(num1, num2):
    return num1 - num2
# Multiplies two numbers
def multiply(num1, num2):
    return num1 * num2
# Divides two numbers
def divide(num1, num2):
    return num1 / num2

while True:
    # Prints the options for the user to take
    print("Select operator:\n" "Add - 1\n" "Subtract - 2\n" "Multiply - 3\n" "Divide - 4\n" "Exit - Z\n")
    # Provides the input for the user to choose
    operator = input("Please enter your choice: ")

    # The If statement that decides whether to end the program (the Z option) or to continue forward
    if operator in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # The addition If statement
        if operator == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        
        # The subtraction If statement
        elif operator == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        
        # The multiplication If statement
        elif operator == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        
        # The division If statement
        elif operator == '4':
            print(num2, "/", num2, "=", divide(num1, num2))
    # The ElseIf statement that terminates the program
    elif operator == 'Z' or 'z':
        quit()
    # The Else statement that indicates an invalid input provided by the user
    else:
        print("Error: Invalid input")