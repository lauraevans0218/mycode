#!/usr/bin/env python3

#add
def add(x,y):
    return x + y

#subtract 
def subtract(x, y):
    return x - y 

#multiply 
def multiply(x, y):
    return x * y 

#divide
def divide(x, y):
    return x / y

operation = input('Chose an Operation(1 - ADD, 2 -SUBTRACT, 3 - MULTIPY, 4 - DIVIDE)')

#take user input to decide operation
if operation in ('1', '2',  '3', '4'):
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: ')) 

    if operation == '1':
        print(add(num1, num2))

    elif operation == '2': 
        print(subtract(num1, num2))

    elif operation == '3':
        print(multiply(num1, num2))

    elif operation == '4':
        print(divide(num1, num2))

    else:
        print("Invalid Choice")
