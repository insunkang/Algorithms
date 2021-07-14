#
#1

def solution(inputString):
    answer = 0
    target = list(str(inputString))
    while True:
        deleteList = list(str(answer))
        for i in deleteList:
            if len(target) > 0 and target[0] == i:
                del target[0]
        if len(target) == 0:
            break
        answer += 1
    print(answer)
    return answer

solution(7234032479947)

#2
# from itertools import combinations
#
# def solution(n, data, limit):
#     answer = []
#     answerlimit = 20000000
#     combis = [i for i in range(1,len(data)+1)]
#     datas = [list(i.split(" ")) for i in data]
#     limits = list(limit.split(" "))
#     print(datas)
#     combiset = list(combinations(combis,n))
#     print(combiset)
#     for i in combiset:
#         timelimit = 0
#         spacelimit = 0
#         now = []
#         num = []
#         for j in i:
#             num.append(int(datas[j-1][1]))
#             now.append(str(datas[j-1][0]))
#             timelimit += int(datas[j-1][2])
#             spacelimit += int(datas[j-1][3])
#         checknum = 0
#         for k in range(1, n+1):
#             if k not in num:
#                 checknum = 1
#         if checknum == 1:
#             continue
#         if int(limits[0]) == 0 or timelimit <= int(limits[0]):
#             if int(limits[1]) == 0 or spacelimit <= int(limits[1]):
#                 if timelimit+spacelimit == answerlimit:
#                     for o in range(n):
#                         if answer[o] == now[o]:
#                             continue
#                         elif answer[o][0] == now[o][0]:
#                             if int(ord(answer[o][1])) < int(ord(now[o][1])):
#                                 break
#                             else:
#                                 answer = now
#                                 break
#                         elif int(ord(answer[o][0])) < int(ord(now[o][0])):
#                             break
#                         elif int(ord(answer[o][0])) > int(ord(now[o][0])):
#                             answer = now
#                             break
#                 elif timelimit+spacelimit < answerlimit:
#                     answerlimit = timelimit+spacelimit
#                     answer = now
#     print(answer)
#
#
#     return answer
#
# solution(2,["a1 1 9 5", "a2 1 9 5", "b1 2 3 3"]	,"0 10")
# # solution(3,	["a1 1 5 5", "b1 2 1 1", "c1 3 5 1"],"10 10")


# #4
# def solution(n, queries):
#     answer = []
#     board = [[] for _ in range(n)]
#     center = 0
#
#     for q in queries:
#         print(center, board)
#         if q[1] != -1:
#             if center == 0:
#                 center = q[1]
#             else:
#                 board[q[0]-1].append(q[1])
#
#         else:
#             if len(board[q[0] - 1]) == 0:
#                 if center == 0:
#                     answer.append(-1)
#                 else:
#                     answer.append(center)
#
#                 check = q[0]
#                 for _ in range(n):
#                     if check == n:
#                         check = 0
#                         if len(board[check]) != 0:
#                             center = board[check][0]
#                             del board[check][0]
#                             break
#                     else:
#                         if len(board[check]) != 0:
#                             center = board[check][0]
#                             del board[check][0]
#                             break
#                     check += 1
#
#                 # if q[0] == n:
#                 #     center = board[0][0]
#                 #     del board[0][0]
#                 # else:
#                 #     center = board[q[0]][0]
#                 #     del board[q[0]][0]
#             else:
#                 answer.append(board[q[0]-1][len(board[q[0]-1])-1])
#                 del board[q[0]-1][len(board[q[0]-1])-1]
#
#
#     print(answer)
#     return answer
#
# # solution(3,[[1,4],[2,2],[1,3],[1,6],[3,-1],[2,-1]])
# # solution(4,[[1,3],[1,2],[3,6],[3,-1],[4,5],[2,-1],[3,-1],[1,-1]])
# solution(5,[[1,-1],[2,-1],[3,-1],[4,-1],[5,-1]])

#3

def solution(endingTime, jobs):
    answer = []
    # for i in jobs:
    #     if i[1]+i[3] < i[2] and i[2] <= endingTime:
    #         answer.append(i[0])
    # print(answer)
    now = 0
    for i in jobs:
        if i[1] > now:
            now = i[1]
        if now+i[3] <= i[2] and now+i[3] < endingTime:
            answer.append(i[0])
        now += i[3] + 1

    # print(answer)
    return answer

# solution(10,[])
solution(40, [[1, 10, 20, 3], [2, 14, 20, 9], [3, 18, 24, 2], [4, 25, 40, 5], [5, 28, 40, 1]])