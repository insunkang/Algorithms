from collections import deque
import copy
r, c = map(int, input().split(" "))

board = []
visited = [[0]*r for _ in range(c)]
result = ["KAKTUS"]
for _ in range(r):
    inputs = list(str(input()))
    board.append(inputs)
start = [0] * 2
end = [0] * 2
water = deque()

for i in range(r):
    for j in range(c):
        if board[i][j] == "D":
            end[0] = i
            end[1] = j
        if board[i][j] == "S":
            start[0] = i
            start[1] = j
        if board[i][j] == "*":
            a = [i,j]
            water.append(a)

visited[start[0]][start[1]] = 1
# print(board[0][0])
dx = [0,0,1,-1]
dy = [-1,1,0,1]


def dfs(board, r, c, start, water):
    water2 = deque()
    while water:
        a, b = water.popleft()
        for i in range(4):
            nowx = a+dx[i]
            nowy = b+dy[i]
            if nowx < r and nowy < c and board[nowx][nowy] != "D":
                board[nowx][nowy] = "*"
                water2.append([nowx,nowy])
    print(board)
    for i in range(4):
        nowx = start[0] + dx[i]
        nowy = start[1] + dy[i]
        if nowx < r and nowy < c and board[nowx][nowy] != "S" and board[nowx][nowy] != "*":
            if board[nowx][nowy] == "D":
                result[0] = "YES"
                return
            board[nowx][nowy] = "S"
            dfs(board,r,c,[nowx,nowy],water2)

dfs(board,r,c,start,water)

print(result[0])



