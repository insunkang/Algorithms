# (점)은 빈 필드를 의미하며, 글자 '#'는 울타리를, 'o'는 양, 'v'는 늑대를 의미한다.
# 한 칸에서 수평, 수직만으로 이동하며 울타리를 지나지 않고 다른 칸으로 이동할 수 있다면, 두 칸은 같은 영역 안에 속한다.
import sys
sys.setrecursionlimit(10**6)

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def find(board,i,j):
    global sheep, wolf
    if 0 > i or i >= r or 0 > j or j >= c or board[i][j] == "-" or board[i][j] == "#":
        return False

    if board[i][j] == "o":
        sheep += 1
    elif board[i][j] == "v":
        wolf += 1
    board[i][j] = "-"
    for k in range(4):
        da = i + dx[k]
        db = j + dy[k]
        if 0 <= da < r and 0 <= db < c and board[da][db] != "-" and board[da][db] != "#":
            find(board, da, db)
    return False
r, c = map(int, input().split(" "))

sheep_cnt, wolf_cnt = 0,0

board = [list(input()) for _ in range(r)]

# print(board)

for i in range(r):
    for j in range(c):
        sheep = 0
        wolf = 0
        find(board,i,j)

        if sheep > wolf:
            sheep_cnt += sheep
        else:
            wolf_cnt += wolf

print(sheep_cnt, wolf_cnt)