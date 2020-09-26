from itertools import  permutations
from itertools import  product
match = [6,2,5,5,4,5,6,3,7,6]
check = [0,0,1,1,1,3,3,1]
answer = 0
k=11
# for i in range(0,100):
#     ea =0
#     for j in range(len(str(i))):
#
#         ea+=match[int(str(i)[j])]
#
#     if ea==k:
#         print(i)
#         answer+=1
# print(answer)

a= k//2
#
# for
#
target =[]
for i in range(1,a):
    ea =0
    for j in product(match,repeat= i):
        ea=sum(j)
        # print(j)
        if ea==k:
            target.append(j)
            answer+=1

result = 0;
target=set(target)
print(target)
print(len(target))
for i in range(len(target)):
    a ={}
    for j in range(len(target[i])):
        a[4]=a[4]+target[i][j]

    for j in range(len(a)):
        result = result+