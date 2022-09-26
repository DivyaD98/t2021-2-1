n = int(input('Enter a number'))
if n % 2 == 0:
    n = n - 1
lst = []
num = 1
while len(lst) < n:
    if num % 2 != 0:
        lst.append(num)
    num = num + 1
print(lst)
