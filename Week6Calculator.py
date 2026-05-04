try:  # everything inside the try block is code that might cause an error(i.e, num2 is zero, or non numeric numbers)
    ## Step 1: Get input - Prompt the user to enter the first number, and operator
    num1 = float(input("Enter the first number: "))
    # Step 2: Prompt the user to enter the operator
    operator = input("Enter the operator (+, -, *, /): ")
    # Step 3: Prompt the user to enter the second number
    num2 = float(input("Enter the second number: "))
    # Step 4: Perform the corresponding operation based on the operator
    # Compute and print directly in each branch
    if operator == '+':
        print(f"result is {num1 + num2}")
    elif operator == '-':
        print(f"result is {num1 - num2}")
    elif operator == '*':
        print(f"result is {num1 * num2}")
    elif operator == '/':
        print(f"result is {num1 / num2}")  # raises ZeroDivisionError if num2 == 0
    else:
        print("Error: Invalid operator.")

except ZeroDivisionError:  # Catches division-by-zero errors that happen in the try block. And displays a friendly message instead of crashing.
    print('You cannot divide by zero')
except ValueError:  # catches non numeric numbers
    print('Please enter a valid number')