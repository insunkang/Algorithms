import copy
import heapq


# def firstQ(money, costs):
#     answer = 0
#     real_money = [1,5,10,50,100,500]
#     real_costs = copy.deepcopy(costs)
#     for i in range(6):
#         costs[i] = (real_money[i] - costs[i])/costs[i]
#     q = []
#     for i in range(6):
#         heapq.heappush(q, (-costs[i], real_money[i]))
#     print(q)
#     for _ in range(6):
#         cost, real_money_temp = heapq.heappop(q)
#         produce_cost = real_costs[costs.index(-cost)]
#         while money >= real_money_temp:
#             money -= real_money_temp
#             answer += produce_cost
#             print(money,answer)
#
#         if money == 0:
#             break
#     print(answer)
#     return answer
# firstQ(4578,[1, 4, 99, 35, 50, 1000])
# firstQ(1999,[2, 11, 20, 100, 200, 600])
# def solution(n, clockwise):
#     answer = [[0]*n for _ in range(n)]
#
#     i = 0
#     j = 0
#     up = [-1,0]
#     down = [1,0]
#     left = [0,-1]
#     right = [0,1]
#     answer[i][j] = 1
#
#     direction_index = 0
#
#     if clockwise:
#         direction = [right, down, left, up]
#     else:
#         direction = [down, right, up, left]
#
#     while True:
#         i += direction[direction_index][0]
#         j += direction[direction_index][1]
#         if answer[i][j] == 0:
#
#
#
#     return answer

# def solution(width, height, diagonals):
#     dp = [[1] * width for _ in range(height)]
#     dp[height-1][width-1] = 0
#     # print(dp)
#     answer = 0
#     directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#     for i in range(height):
#         for j in range(width):
#             if i == 0 and j == 0:
#                 continue
#
#             for direction in directions:
#                 if height > i + direction[0] >= 0 and width > j + direction[1] >= 0:
#                     # print(i + direction[0],j + direction[1])
#                     # print(i,j)
#                     dp[i][j] += dp[i + direction[0]][j + direction[1]]
#     answer = dp[1][1] * dp[height-1][width-1] + dp[2][2] * dp[height-1][width-1]
#     print(answer)
#     return answer
#
# solution(51,37,	[[1,1],[2,2]])

# def solution(n, edges):
#     answer = 0
#     INF = int(1e9)
#     tree = [[INF] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 tree[i][j] = 0
#     for edge in edges:
#         tree[edge[0]][edge[1]] = 1
#         tree[edge[1]][edge[0]] = 1
#     realtree = copy.deepcopy(tree)
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 tree[i][j] = min(tree[i][j], tree[i][k]+tree[k][j])
#     print(realtree)
#     print(tree)
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 if tree[i][j] == tree[i][k] + tree[k][j] and i != j and j!=k and i!=k:
#
#                     print(i,j,k)
#                     answer += 1
#
#
#     return answer
#
# # solution(5,[[0,1],[0,2],[1,3],[1,4]])
# solution(4,[[2,3],[0,1],[1,2]]	)

def solution(width, height, diagonals):
    answer = 0
    route = [[0] * (width) for _ in range(height)]  # 전체 지도를 만든다. 일단 방문한 적이 없으므로 모두 0을 준다.

    route[0][0] = 1  # 시작점으로 가는 방법은 총 1개가 있다. 바로 가만히 있기
    for diagonal in diagonals:
        for i in range(diagonal[0]):  # 1에서 diagonal[0] 자리까지 모든 경우
            for j in range(diagonal[1]):  # 1에서 diagonal[1] 자리까지 모든 경우
                if i == 0 and j == 0:  # 만약, i,j 가 1 일때는 시작 지점이니 스킵
                    continue
                print(route[i - 1][j] + route[i][j - 1])
                route[i][j] += (route[i - 1][j] + route[i][j - 1])
        a = route[diagonal[0]][diagonal[1]]
        print(a)
        route[diagonal[0]][diagonal[1]] = 1
        for i in range(diagonal[0],height):  # 1에서 height 자리까지 모든 경우
            for j in range(diagonal[1],width):  # 1에서 width 자리까지 모든 경우
                if i == 0 and j == 0:  # 만약, i,j 가 1 일때는 시작 지점이니 스킵
                    continue
                route[i][j] += (route[i - 1][j] + route[i][j - 1])
        b = route[-1][-1]
        answer += a*b
    print(answer)
    return (route[-1][-1]) % 100000007

# solution(51,37,	[[17,19]])
# solution(2,2,[[1,1],[2,2]])

def solution(width, height, diagonals):
    route = [[0] * (width + 1) for _ in range(height + 1)]  # 전체 지도를 만든다. 일단 방문한 적이 없으므로 모두 0을 준다.

    route[1][1] = 1  # 시작점으로 가는 방법은 총 1개가 있다. 바로 가만히 있기
    for i in range(1, height + 1):  # 1에서 n의 자리까지 모든 경우
        for j in range(1, width + 1):  # 1에서 m의 자리까지 모든 경우
            if i == 1 and j == 1:  # 만약, i,j 가 1 일때는 시작 지점이니 스킵
                continue
            else:  # 왼쪽으로 들어오는 경우와 위쪽에서 들어오는 경우를 합한다.
                route[i][j] += (route[i - 1][j] + route[i][j - 1])
    print(route)
    print(route[height][width])
    return (route[-1][-1]) % 100000007

solution(2,2,[[1,1],[2,2]])