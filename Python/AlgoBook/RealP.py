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

# a = input()

# result = int(a[0])

# for i in range(1,len(a)):
#     if a[i]==0 or a[i]==1 or result==1 or result==0:
#         result += int(a[i])
#     else:
#         result *= int(a[i])
    
# print(result)

# reverse string

# s = input()
# result = 0
# a= s[0]
# for i in range(1,len(s)):
#     if a!=s[i]:
#         result+=1
#         a =s[i]

# result = result//2

# print(result)

# Unavailable cost

# n = int(input())
# money = list(map(int, input().split()))
# result = sum(money)+1
# test = result
# while True:


#     result+=1

# select bowling ball

n,m = map(int, input().split())

balls = list(map(int, input().split()))

result = 0

for i in range(len(balls)):
    for j in range(i,len(balls)):
        if balls[i]!=balls[j]:
            result+=1

print(result)