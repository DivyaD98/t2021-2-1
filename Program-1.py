def calculator(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return add, sub, mul, div
a = int(input('Enter first number'))
b = int(input('Enter second number'))
p, q, r, s = calculator(a, b)
print(p,end=' ')
print(q,end=' ')
print(r,end=' ')
print(s,end=' ')
