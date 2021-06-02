import sys
input = sys.stdin.readline

def dfs(board, rivers, now):
    board[now]

t = int(input())

k,m,p = map(int, input().split(" "))

rivers = [0] * (m + 1)

board = [[] for _ in range(m + 1)]

for _ in range(p):
    a,b = map(int, input().split(" "))
    board[b].append(a)

print(board)

for i in range(1,len(board)):
    if len(board[i]) == 0:
        rivers[i] = 1

print(rivers)
