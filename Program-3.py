# With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]



a = int(input('Enter a number'))
if a % 2 == 0:
    a -=1
i = 1
while a > 0:
    print(i,end=" ")
    i = i + 2
    a = a - 1
