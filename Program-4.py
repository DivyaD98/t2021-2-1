''' Get the total count of number list in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
    (examples)
    input: [1,2,8,9,12,46,76,82,15,20,30]
    Output:
        {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}
'''

a=[1,2,3,4,5,6,7,8,9]
data=[1,2,8,9,12,46,76,82,15,20,30]
lst=[]
count=0
for i in a:
    for j in data:
        if j%i==0:
            count+=1
    lst.append(count)
    count=0
result=dict(zip(a,lst))
print(result)
