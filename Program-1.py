''' 
Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
    Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
    Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string
'''

#Calculator

class Calculator:
    def __init__(self, a, b, type_of_operation):

        self.int_1 = a
        self.int_2 = b
        self.type_of_operation = type_of_operation

        if (type_of_operation == '+'):
            print(a, '+', b, '=', a + b)

        if (type_of_operation == '-'):
            print(a, '-', b, '=', a - b)

        if (type_of_operation == '*'):
            print(a, '*', b, '=', a * b)

        if (type_of_operation == '/'):
            if b != 0:
                print(a, '/', b, '=', a / b)
            else:
                print("Anything cannot be divided by Zero")


a = float(input('Enter first number: '))
b = float(input('Enter second number: '))
type_of_operation = str(input('Enter a type of operation: +--> Add, \'-\'--> Subtract, *--> Multiply, /--> Divide'))
p1 = Calculator(a, b, type_of_operation) 
