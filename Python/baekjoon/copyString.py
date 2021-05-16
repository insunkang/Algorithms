# abaabba
# aaabbbabbbaaa

a = str(input())
b = str(input())
result = [0] * len(b)

for i in range(len(b)):
    j = i+2
    check = 1
    while j <= len(b):
        if b[i:j] in a:
            check += 1
            j += 1
        else:
            break
    result[i] = check

print(result)

take = 0
nowIndex = 0
while True:
    nowIndex += result[nowIndex]
    take += 1
    if nowIndex > len(b)-1:
        break

print(take)

# from collections import deque
#
# s = input()
# p = input()
# ans = 0
#
# q = deque()
# q.append('')
# while q:
#     now = q.popleft()
#     if now == p:
#         break
#
#     for i in range(len(p) - 1, len(now) - 1, -1):
#         print(i, p[len(now):i + 1])
#         if p[len(now):i + 1] in s:
#             ans += 1
#             now += p[len(now):i + 1]
#             q.append(now)
#             break
#
# print(ans)
# print(result)
# print(dp)

# for i in range(len(b)):
#     for j in range(result[i],0,-1):
#         if j+i <len(b) and dp[i]+1 < dp[j+i]:
#             dp[j+i] = dp[i]+1
# print(dp)
# print(dp[len(b)-1])