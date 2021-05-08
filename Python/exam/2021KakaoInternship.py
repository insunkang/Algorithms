# from collections import deque
# #1
#
# def solution(s):
#     answer = ""
#     q = deque()
#     strings = ["zero","one","two","three","four","five","six","seven","eight","nine"]
#     numbers = ["0","1","2","3","4","5","6","7","8","9"]
#     a = ""
#     for i in range(len(s)):
#         if s[i] in numbers:
#             answer += s[i]
#         else:
#             a += s[i]
#         if a in strings:
#             answer += numbers[strings.index(a)]
#             a = ""
#     print(answer)
#
#
#     # return answer
#
# solution("one4seveneight")


#2
# def find(place):
#     answer = []
#
#     for i in range(5):
#         for j in range(5):
#             if place[i][j] == "P":
#                 answer.append([i,j])
#
#     return answer
#
#
# def solution(places):
#     answer = [1] * 5
#     for i in range(5):
#         checkplace = places[i]
#         place = [[0 for col in range(5)] for row in range(5)]
#         for p in range(5):
#             for o in range(5):
#                 place[p][o] = checkplace[p][o]
#
#         person = find(place)
#         print(person)
#
#         for j in range(len(person)):
#
#             if answer[i] == 0: # 거리두기 못지킬때 다른사람 다 체크 안하게끔
#                 break
#
#             for k in range(j+1,len(person)):
#
#                 if answer[i] == 0: # 거리두기 못지킬때 다른사람 다 체크 안하게끔
#                     break
#
#                 check = abs(person[j][0]-person[k][0]) + abs(person[j][1]-person[k][1])
#                 if check == 1: # 거리두기 못지킬때
#                     answer[i] = 0
#
#                 elif check == 2:
#                     secondCase = [person[j][0],person[j][1],person[k][0],person[k][1]]
#
#                     #2
#                     if secondCase.count(person[j][0]) == 3 and place[(person[j][0]+person[k][0])//2][(person[j][1]+person[k][1])//2] == "O":
#                         answer[i] = 0
#                         break
#                     elif secondCase.count(person[j][1]) == 3 and place[(person[j][0]+person[k][0])//2][(person[j][1]+person[k][1])//2] == "O":
#                         answer[i] = 0
#                         break
#                     elif secondCase.count(person[k][0]) == 3 and place[(person[j][0]+person[k][0])//2][(person[j][1]+person[k][1])//2] == "O":
#                         answer[i] = 0
#                         break
#                     elif secondCase.count(person[k][1]) == 3 and place[(person[j][0]+person[k][0])//2][(person[j][1]+person[k][1])//2] == "O":
#                         answer[i] = 0
#                         break
#                     # 1
#
#                     elif place[person[j][0]][person[k][1]] == "O" or place[person[k][0]][person[j][1]] == "O":
#                         answer[i] = 0
#                         break
#                     # # 1-2
#                     # elif person[j][0] != person[j][1] and place[person[j][0]][person[j][0]] == "O" or place[person[j][1]][person[j][1]] == "O":
#                     #     answer[i] = 0
#                     #     break
#
#
#
#     print(answer)
#
# solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])

#3
from collections import deque
def solution(n, k, cmd):
    answer = ''
    q = deque()
    result = ["O"] * n

    for i in range(len(cmd)):

        command = list(map(str, cmd[i].split(" ")))
        print(command)
        print(k)
        print(result)
        if len(command) == 1:
            if command[0] == "C":
                result[k] = "X"
                q.append(k)

                if result[k:].count("O") == 0:
                    while True:
                        k -= 1
                        if result[k] =="O":
                            break
                else:
                    while True:
                        k += 1
                        if result[k] == "O":
                            break

            elif command[0] == "Z":
                check = q.pop()
                result[check] = "O"
        else:
            if command[0] == "D":
                check = int(command[1])
                while check != 0:
                    k += 1
                    if result[k] == "O":
                        check -= 1
                # check = result[k+1:k+1+int(command[1])].count("X")
                # k += (int(command[1]) + check)
            elif command[0] == "U":
                check = int(command[1])
                while check != 0:
                    k -= 1
                    if result[k] == "O":
                        check -= 1
                # check = result[k - int(command[1]):k].count("X")
                # k -= (int(command[1])+check)

    print(result)
    return answer
# solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
# solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])


import copy
import heapq

da = [float('inf')]


def dfs(now,end,road,traps,result,cost,visited,nodes):
    if now == end:
        da[0] = min(da[0], result)
        return
    # if da[0] > result:
    #     return
    if visited[now] > 2 and now in nodes:
        return
    if now in traps:
        for i in road:
            if now in i:
                temp = i[0]
                i[0] = i[1]
                i[1] = temp
    cVisited = copy.deepcopy(visited)
    cVisited[now] += 1
    cRoad = copy.deepcopy(road)
    for i in range(len(cRoad)):
        if now == cRoad[i][0]:

            dfs(cRoad[i][1],end,cRoad,traps,result+cost[i],cost,cVisited,nodes)


def solution4(n, start, end, roads, traps):
    answer = 0
    visited = [0] * (n + 1)
    cost = [roads[i][2] for i in range(len(roads))]
    road = [[roads[i][0],roads[i][1]] for i in range(len(roads))]
    node = [0] * (n+1)
    nodes = []

    for i in road:
        node[i[0]] += 1
        node[i[1]] += 1
    for i in range(len(node)):
        if node[i] == 1:
            nodes.append(i)
    print(nodes)
    print(cost)
    print(road)
    dfs(start,end,road,traps,0,cost,visited,nodes)
    print(da[0])
    return answer

# def solution4(n, start, end, roads, traps):
#     answer = 0
#     visited = [0] * (n)
#     cost = [roads[i][2] for i in range(len(roads))]
#     road = [[roads[i][0],roads[i][1]] for i in range(len(roads))]
#     # print(cost)
#     # print(road)
#     # dfs(start,end,road,traps,0,cost,visited)
#     q = []
#     for i in range(len(road)):
#         if road[i][0] == start:
#             heapq.heappush(q,(cost[i],road[i][1]))
#     # print(q)
#     while q:
#         print(q)
#         dist, now = heapq.heappop(q)
#         print(str(dist)+","+str(now))
#         answer += dist
#         if now == end:
#             break
#         if visited[now] > 3:
#             continue
#         if now in traps:
#             for i in road:
#                 if now in i:
#                     temp = i[0]
#                     i[0] = i[1]
#                     i[1] = temp
#         for i in range(len(road)):
#             if now == road[i][0]:
#                 heapq.heappush(q,(cost[i],road[i][1]))
#
#     print(answer)
#     # print(da[0])
#     return answer
#
solution4(3,1,3,[[1, 2, 2], [3, 2, 3]],[2])
# solution4(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2,3])