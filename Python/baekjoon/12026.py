# import sys


# n = int(input())

# target = str(input())

# BOJ = ['B','O','J']

# result = 0
# now = 1
# plus = 1
# for i in range(1,len(target)):
#     print(plus, target[i], BOJ[now])
#     if target[i] == BOJ[now]:
#         result += (plus * plus)
#         plus = 1
#         if now == 2:
#             now = 0
#         else:
#             now += 1
#     else:
#         if i == len(target)-1:
#             result = -1
#             break
#         plus += 1

    


# print(result)

n = int(input())
lst = input()

MAX = 999999999
dp = [MAX] * n

def get_prev(x):
    if x == "B":
        return "J"
    elif x == "O":
        return "B"
    elif x == "J":
        return "O"

dp[0] = 0
for i in range(1, n):
    prev = get_prev(lst[i])
    for j in range(i):
        if lst[j] == prev:
            dp[i] = min(dp[i], dp[j] + pow(i - j, 2))
print(dp[n - 1] if dp[n - 1] != MAX else -1)