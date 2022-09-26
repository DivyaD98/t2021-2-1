''' 
Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
    Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
    Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string
'''

#Calculator

a = float(input("Enter 1st number :"))
b = float(input("Enter 2nd number :"))
type_of_operation = str(input("Enter type of operation : +--> Add, \'-\'--> Subtract, *--> Multiply, /--> Divide "))

if type_of_operation == "+":
    print(a, '+', b, '=', a + b)
elif type_of_operation == "-":
    print(a, '-', b, '=', a - b)
elif type_of_operation == "*":
    print(a, '*', b, '=', a * b)
elif type_of_operation == "/":
    if b != 0:
        print(a, '/', b, '=', a / b)
    else:
        print("Invalid input") 

