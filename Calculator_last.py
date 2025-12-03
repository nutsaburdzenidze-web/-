def calculate(num1, num2, operation):
    if operation == '*':
        return num1 * num2
    elif operation == '/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            print("Division by zero!!!")
            return None
    elif operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2

def get_input():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter operation you want to perform: ")
            if operation not in ['+', '-', '*', '/']:
                print("invalid operation.")
                continue
            return num1, num2, operation
        except ValueError:
            print("Please enter real numbers!")
num1, num2, operation = get_input()
print(f"{num1} {operation} {num2} = {calculate(num1, num2, operation)}")
