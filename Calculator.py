def calculate():
    num1 = int(input('Enter your first number: '))
    num2 = int(input('Enter your second number: '))

    print('{} + {} = '.format(num1, num2))
    print(add(num1, num2))

    print('{} - {} = '.format(num1, num2))
    print(subtract(num1, num2))

    print('{} * {} = '.format(num1, num2))
    print(multiply(num1, num2))

    print('{} / {} = '.format(num1, num2))
    print(divide(num1, num2))

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x,y):
    return x/y

def multiply(x,y):
    return x*y

calculate()