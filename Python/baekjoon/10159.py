# from collections import deque
#
# n = int(input())
# m = int(input())
# result = [[i] for i in range(n+1)]
# cals = [0] * (n+1)
#
# # parents = [0] * (n+1)
#
# for _ in range(m):
#     a,b = map(int,input().split(" "))
#     cals[a] = b
#     result[a].append(b)
#     # parents[b] = a
#
# # print(result)
#
# # print(parents)
#
# # print(cals)
#
# for i in range(1,n+1):
#     q = deque()
#     if cals[i] != 0:
#         q.append(cals[i])
#     nowcheck = [i]
#     # print(result)
#     while q:
#         now = q.popleft()
#         for j in nowcheck:
#             if now not in result[j]:
#                 result[j].append(now)
#             if j not in result[now]:
#                 result[now].append(j)
#         nowcheck.append(now)
#
#         if cals[now] != 0:
#             q.append(cals[now])
#
# # print(result)
#
# for i in range(1, n+1):
#     print(n-len(result[i]))
import sys

input = sys.stdin.readline


def floydWarshall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if adjMatrix[i][k] and adjMatrix[k][j]:
                    adjMatrix[i][j] = 1


N = int(input())
M = int(input())

adjMatrix = [[0] * N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())

    adjMatrix[a - 1][b - 1] = 1

floydWarshall()

for i in range(N):
    ans = 0

    for j in range(N):
        if i == j:
            continue

        if not adjMatrix[i][j] and not adjMatrix[j][i]:
            ans += 1

    print(ans)