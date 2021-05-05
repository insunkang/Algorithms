import copy
from itertools import permutations

# +, -, *
def cal(express, a,b):
    if express == "+":
        return  a+b
    elif express == "-":
        return a-b
    else:
        return a*b


def solution(expression):
    answer = 0

    strings = ["+", "-", "*"]

    expressList = []
    checkSum = ""
    for i in range(len(expression)):
        if expression[i] in strings:
            expressList.append(int(checkSum))
            expressList.append(expression[i])
            checkSum = ""
        elif i == len(expression)-1:
            checkSum += expression[i]
            expressList.append(int(checkSum))
        else:
            checkSum += expression[i]
    # print(expressList)
    permuSet = [0,1,2]
    #
    # print(expressList[:2])
    # print(expressList[2:4])
    permute = list(permutations(permuSet))
    # print(permute)
    for i in range(len(permute)):
        copyList = copy.deepcopy(expressList)

        for j in range(3):
            # print(strings[permute[i][j]])
            while strings[permute[i][j]] in copyList:
                if len(copyList) == 3:
                    answer = max(abs(answer), abs(cal(copyList[1],copyList[0],copyList[2])))
                    break
                else:
                    jndex = copyList.index(strings[permute[i][j]])
                    a = copyList[:jndex -1]
                    b = copyList[jndex+2: ]
                    a.append(cal(copyList[jndex],copyList[jndex-1],copyList[jndex+1]))
                    copyList = a+b
                    # print(copyList)









    print( answer)



solution("100-200*300-500+20")