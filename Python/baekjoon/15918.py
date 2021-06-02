# from itertools import permutations, combinations
# import copy
# answer = 0
# n,x,y = map(int,input().split(" "))
#
# for i in range(1,n+1):
#     target = [0] * (2 * n)
#     target[x-1], target[y-1] = i, i
#     checklist = []
#
#     for j in range(1,n+1):
#         if j != i:
#             checklist.append(j)
#             checklist.append(j)
#
#     tempperm = list(permutations(checklist,len(checklist)))
#     perm = []
#     for u in tempperm:
#         temp = []
#         for m in u:
#             temp.append(m)
#         if temp not in perm:
#             perm.append(temp)
#     print(perm)
#     for j in range(len(perm)):
#         nowperm = []
#         for k in perm[j]:
#             nowperm.append(k)
#         nowperm.insert(x-1, i)
#         nowperm.insert(y-1, i)
#         print(nowperm)
#         result = 1
#         for p in range(1,n+1):
#             if nowperm[nowperm.index(p)+p+1] != p:
#                 result = 0
#                 break
#         answer += result
#         # visited = [0] * len(target)
#
# print(answer)
#
#
#
#
#
import sys

input = sys.stdin.readline

N, X, Y = map(int, input().split())
used = [False] * (N + 1)
arr = [0] * (2 * N + 1)
used[Y - X - 1] = True
arr[X] = Y - X - 1
arr[Y] = Y - X - 1
answer = 0


def dfs(x):
    print(arr, x)
    global answer
    if x == 2 * N + 1:
        answer += 1
        return
    if arr[x] != 0:
        dfs(x + 1)
    else:
        for j in range(1, len(used)):
            if not used[j] and x + j + 1 < 2 * N + 1 and arr[x + j + 1] == 0:
                used[j] = True
                arr[x] = j
                arr[x + j + 1] = j
                dfs(x + 1)
                used[j] = False
                arr[x] = 0
                arr[x + j + 1] = 0


dfs(1)
print(answer)