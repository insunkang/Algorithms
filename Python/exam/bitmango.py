# from itertools import permutations
#
# def solution(n, capacity, files):
#     answer = 0
#     capa = []
#
#     for i in range(len(files),0,-1):
#         a = list(permutations(files,i))
#         for j in a:
#             if sum(j)<=capacity:
#                 if len(capa) == 0:
#                     capa.append(j)
#                 else:
#                     compare = 0
#                     for k in range(j):
#                        for b in capa:
#                            if k in capa:
#                                 compare = 1
#                     if compare == 0:
#
#
#
#
#
#     return answer
#
# capa = [[0,0] for k in range(2)]
# print(capa)

# --------------------------------------------------

# import sys
# from collections import deque
# input = sys.stdin.readline
#
# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=' ')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
#
# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]
# visited = [False] * 9
#
# dfs(graph, 1, visited)

# import copy
# def dfs(board, x, y, n, alpha):
#     if x <= -1 or x >=n or y <= -1 or y >= n:
#         return False
#     if board[x][y] !=  "0" and board[x][y]==alpha:
#         board[x][y] = "0"
#         dfs(board, x - 1, y, n, alpha)
#         dfs(board, x, y - 1, n, alpha)
#         dfs(board, x + 1, y, n, alpha)
#         dfs(board, x, y + 1, n, alpha)
#         return True
#
#     return False
#
# def solution(board):
#     boardk = []
#
#     for i in range(len(board)):
#         sp = []
#         for k in range(len(board[i])):
#             sp.append(board[i][k])
#
#         boardk.append(sp)
#
#     print(boardk)
#     answer = 0
#
#     a = 0
#     b = 0
#     # 위에서
#     for i in range(len(board)):
#         copyB = copy.deepcopy(boardk)
#         for k in range(len(board)):
#             if copyB[i][k] != "0":
#                 dfs(copyB,i,k, len(board), copyB[i][k])
#         result = 0
#         for o in range(len(board)):
#             for p in range(len(board)):
#                 if copyB[o][p] == "0":
#                     result += 1
#         if result > a:
#             a = result
#     # 왼쪽에서
#     for j in range(len(board)):
#         copyB = copy.deepcopy(boardk)
#         for k in range(len(board)):
#             if copyB[k][j] != "0":
#                 dfs(copyB,j,k, len(board), copyB[j][k])
#         result = 0
#         for o in range(len(board)):
#             for p in range(len(board)):
#                 if copyB[o][p] == "0":
#                     result += 1
#         if result > b:
#             b = result
#
#     answer = max(a,b)
#     print(answer)
#     return answer
#
# solution(["DDCCC","DBBBC","DBABC","DBBBC","DDCCC"])

def porp(board, check, s1):
    if check<len(board):
        # check+=1
        if board[check] == "p":
            a = []
            for _ in range(4):
                check+=1
                a.append(board[check])
            s1.append(a)

        else:
            a = []
            for _ in range(4):
                a.append(board[check])
            s1.append(a)
        check += 1
        porp(board, check, s1)
        return True

    else:
        return False


def solution(S1, S2):
    answer = 0
    s1 = []
    s2 = []
    i = 0
    k = []

    if S1[0] == "p":
        i+=1
        porp(S1,i,s1)

    else:
        a = []
        for _ in range(4):
            a.append(S1)
        for _ in range(4):
            s1.append(a)


    i = 0
    if S2[0] == "p":
        i+=1
        porp(S2,i,s2)

    else:
        a = []
        for _ in range(4):
            a.append(S2)
        for _ in range(4):
            s2.append(a)
    print(s1)
    print(s2)

    for u in range(4):
        for y in range(4):
            if s1[u][y] =="b" or s2[u][y] == "b":
                answer +=1

    answer = answer * 64
    print(answer)
    return answer

solution("b","w")