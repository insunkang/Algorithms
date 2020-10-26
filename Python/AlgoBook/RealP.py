# adventure guild

# n = int(input())

# person = list(map(int, input().split()))

# person.sort()
# print(person)
# result = 0
# check = 0
# sumP = 0
# for i in range(len(person)):
#     check+=1
#     sump=person[i]
#     if sump/check==1:
#         result+=1
#         check=0
#         sumP=0
#         print(i)

# print(result)

# multiply or plus

a = input()

result = int(a[0])

for i in range(1,len(a)):
    if a[i]==0 or a[i]==1 or result==1 or result==0:
        result += int(a[i])
    else:
        result *= int(a[i])
    
print(result)