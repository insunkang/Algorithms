import copy

#    왼,위,오,아래
dx = [0,1,0,-1]
dy = [-1,0,1,0]
da = [float('inf')]
# 0 1 2 3
# 왼,위,오,아래

def find(a, b, n, board, visited, dir, result):
    # print(visited)
    for i in range(4):
        covisit = copy.deepcopy(visited)
        nx = a + dx[i]
        ny = b + dy[i]
        if n > nx > -1 and n > ny > -1 and board[nx][ny] == 0 and covisit[nx][ny] == 0:
            if i == dir or dir == -1:
                result += 100
            else:
                result += 500

            if nx == n - 1 and ny == n - 1:
                # print(result)
                da[0] = min(da[0], result)
                return
            covisit[a + dx[i]][b + dy[i]] = 1
            find(a + dx[i], b + dy[i], n, board, covisit, i, result)





def solution(board):


    visited = [[0 for col in range(len(board))] for row in range(len(board))]

    visited[0][0] = 1
    print(visited)
    find(0, 0, len(board), board, visited, -1, 100)


    print(da[0])





solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])