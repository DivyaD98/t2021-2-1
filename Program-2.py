# With a single integer as the input, generate the following until a = x [series of numbers as shown in the below examples]
   '''
    Output: (examples)
        1) input a = 1, then output : 1
        2) input a = 2, then output : 1, 3
        3) input a = 3, then output : 1, 3, 5
        4) input a = 4, then output : 1, 3, 5, 7
        .
        .
        5) input a = x, then output : 1, 3, 5, 7, .......
   '''

# Code

a = int(input('Enter a number'))
i = 1
while a > 0:
    print(i, end=" ")
    i = i + 2
    a = a - 1
