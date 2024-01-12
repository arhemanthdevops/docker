from random import randint

def perform_operation(min_number, max_number, operation):
    if operation == 'add':
        return min_number + max_number
    elif operation == 'subtract':
        return max_number - min_number
    elif operation == 'multiply':
        return min_number * max_number
    elif operation == 'random':
        return randint(min_number, max_number)

# User input for the numbers
min_number = int(input('Please enter the min number: '))
max_number = int(input('Please enter the max number: '))

# Check if the maximum number is less than the minimum number
if max_number < min_number:
    print('Invalid input - max number should be greater than or equal to min number. Shutting down...')
else:
    # User input for the desired operation
    print("Choose an operation: add, subtract, multiply, random")
    operation = input("Enter the operation: ").lower()

    # Check if the operation is valid
    if operation in ['add', 'subtract', 'multiply', 'random']:
        result = perform_operation(min_number, max_number, operation)
        print(f"The result is: {result}")
    else:
        print("Invalid operation. Shutting down...")

