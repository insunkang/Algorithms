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
# money.sort()
# target = 1

# for x in money:
#     if target<x:
#         break
#     target += x

# print(target)
# select bowling ball

# n,m = map(int, input().split())

# balls = list(map(int, input().split()))

# result = 0

# for i in range(len(balls)):
#     for j in range(i,len(balls)):
#         if balls[i]!=balls[j]:
#             result+=1

# print(result)

# 무지의 먹방 라이브

# import heapq

# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1
    
#     q = []
#     for i in range(len(food_times)):
#         heapq.heappush(q,(food_times[i], i + 1))

#     sum_value = 0
#     previous = 0
#     length = len(food_times)

#     while sum_value + ((q[0][0] - previous) * length) <= k:
#         now = heapq.heappop(q)[0]
#         sum_value += (now - previous) * length
#         length -= 1
#         previous = now

#     result = sorted(q, key = lambda x: x[1])
#     return result[(k - sum_value) % length][1]

# lucky straight

command = str(input())

length = len(command)



a = command[0:length//2]
b = command[length//2:]

print(a,b)
reA = 0 
reB = 0
for i in a:
    reA += int(i)
for i in b:
    reB += int(i)

if reA==reB:
    print("LUCKY")
else:
    print("READY")
