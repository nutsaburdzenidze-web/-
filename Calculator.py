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
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation you want to perform: ")
        while not (operation in['+','-','*','/']):
            print("Please enter valid operation!")
    except TypeError:
        print("Please enter real numbers!")
    return num1, num2, operation
num1, num2, operation = get_input()
print(f"{num1} {operation} {num2} = {calculate(num1, num2, operation)}")