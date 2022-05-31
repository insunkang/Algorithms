import copy


def solution1(v, a, b):
    answer = 0

    while True:
        v.sort(reverse=True)
        if v[0] < a or min(v[1:]) < b:
            break
        else:
            v[0] -= a
            for i in range(1,len(v)):
                v[i] -= b
        answer += 1
    print(answer)
    return answer


# solution1([4, 5, 5], 2, 1)

def solution2(logs):
    answer = []
    keys = []
    values = []
    valuesofvalues=[]
    for log in logs:
        loginfo = log.split(" ")
        if loginfo[0] in keys:
            # print(loginfo[1] in values)
            if loginfo[1] in values[keys.index(loginfo[0])]:
                valuesofvalues[keys.index(loginfo[0])][values[keys.index(loginfo[0])].index(loginfo[1])] = loginfo[2]

                # print(values)
                # print(valuesofvalues)
            else:
                values[keys.index(loginfo[0])].append(loginfo[1])
                valuesofvalues[keys.index(loginfo[0])].append(loginfo[2])
                # print(values)
                # print(valuesofvalues)
        else:
            keys.append(loginfo[0])
            values.append([loginfo[1]])
            valuesofvalues.append([loginfo[2]])
            # print(values)
            # print(valuesofvalues)
    # print(keys,values,valuesofvalues)
    #
    for i in range(len(values)):
        for j in range(i+1,len(values)):
            if len(values[i]) == len(values[j]):
                if len(values[i]) <5:
                    break
                same = 1
                for o in values[i]:
                    if o not in values[j]:
                        same = 0
                        break
                if same == 1:
                    samevalue = 1
                    for k in values[i]:
                        if valuesofvalues[i][values[i].index(k)] != valuesofvalues[j][values[j].index(k)]:
                            samevalue = 0
                            break
                    if samevalue == 1:
                        if keys[i] not in answer:
                            answer.append(keys[i])
                        if keys[j] not in answer:
                            answer.append(keys[j])
    answer.sort()
    if len(answer) == 0:
        answer.append("None")
    print(answer)

    return answer
# solution2(["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"])
# solution2(["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "1101 1 95", "1101 2 100", "1101 4 100", "1101 7 100", "1101 9 100", "1102 1 95", "1102 2 100", "1102 4 100", "1102 7 100", "1102 9 100"])
# solution2(["1901 10 50", "1909 10 50"])
# solution2(["0001 1 0", "0001 2 0", "0001 3 0", "0001 4 0", "0001 5 0", "0456 1 0", "0456 2 0", "0456 3 0", "0456 4 0", "0456 5 0"])

# def pop_num(b, m, n):
#     pop_set = set()
#     # search
#     for i in range(1, n):
#         for j in range(1, m):
#             if b[i][j] == b[i - 1][j - 1] == b[i - 1][j] == b[i][j - 1] != '_':
#                 pop_set |= set([(i, j), (i - 1, j - 1), (i - 1, j), (i, j - 1)])
#     # set_board
#     for i, j in pop_set:
#         b[i][j] = 0
#     for i, row in enumerate(b):
#         empty = ['_'] * row.count(0)
#         b[i] = empty + [block for block in row if block != 0]
#     return len(pop_set)
#
#
# def solution(board):
#     count = 0
#     m = 6
#     n = 6
#     b = list(map(list, zip(*board)))
#     while True:
#         pop = pop_num(b, m, n)
#         if pop == 0: return count
#         count += pop


def pop_num(board,check,checked,m,n):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    print(board)
    check[m][n] = 1

    for k in range(4):
        dxx = m+dx[k]
        dyy = n+dy[k]
        if 6>dxx>=0 and 6>dyy>=0 and board[dxx][dyy] == board[m][n] and check[dxx][dyy] == 0:
            checked.append([m,n])
            pop_num(board,check,checked,dxx,dyy)

    again = 0
    if len(checked) >= 3:
        for i in checked:
            board[i[0]][i[1]] = 0
        again = 1

    if again == 1:
        for i in range(6):
            if max([board[0][i], board[1][i], board[2][i], board[3][i], board[4][i], board[5][i]]) != 0:
                for j in range(1, 6):
                    if board[j][i] != 0:
                        temp = j - 1
                        while True:
                            if board[temp][i] != 0:
                                board[temp + 1][i] = board[j][i]
                                board[j][i] = 0
                                break
                            else:
                                temp -= 1
        check = [[0] * 6 for _ in range(6)]
        pop_num(board, check, [], 0, 0)
    return board



def solution4(macaron):
    board = [[0] * 6 for _ in range(6) ]

    # print(board)
    for i in macaron:
        for j in range(6):
            if board[j][i[0] - 1] == 0:
                board[j][i[0] - 1] = i[1]
                break
        for m in range(6):
            for n in range(6):
                if board[m][n] != 0:
                    check = [[0] * 6 for _ in range(6)]
                    pop_num(board,check,[],m,n)
    # print(board)
# solution4([[1,1],[2,1],[1,2],[3,3],[6,4],[3,1],[3,3],[3,3],[3,4],[2,1]])
solution4([[1,1],[1,2],[1,4],[2,1],[2,2],[2,3],[3,4],[3,1],[3,2],[3,3],[3,4],[4,4],[4,3],[5,4],[6,1]])