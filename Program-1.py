''' 
Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
    Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
    Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string
'''

#Calculator

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print("Select any operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = (input("Enter choice(1,2,3,4): "))
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first value: "))
        num2 = float(input("Enter the second value: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", mul(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", div(num1, num2))
        break
    else:
        print("Invalid Input")

