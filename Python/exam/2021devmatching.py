# def solution(lottos, win_nums):
#     answer = []
#     rank = [6,5,4,3,2]
#
#     check = 0
#
#     for i in lottos:
#         if i in win_nums:
#             check += 1
#
#     zero = lottos.count(0)
#
#     if check+zero not in rank:
#         answer.append(6)
#     else:
#         answer.append(rank.index(check + zero) + 1)
#
#     if check not in rank:
#         answer.append(6)
#     else:
#         answer.append(rank.index(check) + 1)
#
#
#
#     print(answer)

# solution([44, 1, 0, 0, 31, 25],	[31, 10, 45, 1, 6, 19])

def rotate(rows, colums, x1, y1, x2, y2):

    originIndexes = []
    changeIndexes = []
    values = []

    # 윗면
    for i in range(y1 - 1, y2 - 1):
        values.append(box[x1 - 1][i])
        originIndexes.append([x1 - 1, i])

    # 오른면
    for i in range(x1 - 1, x2 - 1):
        values.append(box[i][y2 - 1])
        originIndexes.append([i, y2 - 1])

    #아랫면
    for i in range(y2 - 1, y1 - 1, -1):
        values.append(box[x2 - 1][i])
        originIndexes.append([x2 - 1, i])
        
    # 왼쪽면
    for i in range(x2 - 1, x1 - 1, -1):
        values.append(box[i][y1 - 1])
        originIndexes.append([i, y1 - 1])

    for i in range(1,len(originIndexes)):
        changeIndexes.append(originIndexes[i])

    changeIndexes.append(originIndexes[0])

    print(originIndexes)
    print(changeIndexes)

    for i in range(len(changeIndexes)):
        box[changeIndexes[i][0]][changeIndexes[i][1]] = values[i]

    print(values)

    return min(values)

def solution2(rows, columns, queries):
    answer = []
    global box
    box = []

    number = 1
    for i in range(1, rows + 1):
        row = []
        for j in range(1, columns + 1):
            row.append(number)
            number += 1
        box.append(row)

    for i in range(len(queries)):
        answer.append(rotate(rows, columns, queries[i][0], queries[i][1], queries[i][2], queries[i][3]))

    print(answer)


    # return answer

# solution2(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])


from collections import deque
import copy


def solution3(enroll, referral, seller, amount):
    v = len(enroll)
    indegree = [0] * (v)
    graph = [[] for i in range(v)]
    money = [0] * (v)
    last = []
    for i in range(v):
        if referral[i] != "-":
            graph[i].append(referral[i])
            indegree[enroll.index(referral[i])] += 1
        else:
            last.append(enroll[i])
    print(graph)
    print(indegree)

    q = deque()

    for i in range(v):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        print(now)
        if len(graph[now]) == 0:

            if enroll[now] in seller:
                    money[now] += (amount[seller.index(enroll[now])])
                    money[now] *= 90
            else:
                money[now] *= 0.9

        else:
            for i in graph[now]:
                print(i)
                if i in seller:
                    if i in last:
                        money[enroll.index(i)] += amount[seller.index(i)]
                        money[enroll.index(i)] *= 0.9
                    else:
                        money[enroll.index(referral[i])] += (amount[seller.index(i)])
                else:
                    if money[enroll.index(i)] != 0:
                        money[enroll.index(referral[i])] += (amount[seller.index(i)])
                # print(enroll.index(i))
                indegree[enroll.index(i)] -= 1

                if indegree[enroll.index(i)] == 0:
                    q.append(enroll.index(i))


    print(money)
    # answer = []
    # return answer

solution3(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10])