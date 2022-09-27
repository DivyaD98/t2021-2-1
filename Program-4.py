a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
lst = []
count = 0
for i in a:
    for j in data:
        if j % i == 0:
            count += 1
    lst.append(count)
    count = 0
result = dict(zip(a, lst))
print(result)
