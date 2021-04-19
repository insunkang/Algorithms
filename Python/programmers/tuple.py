def solution(s):
    answer = []
    s = s[1:len(s)-1]
    sList = list(map(str,s.split("},{")))
    sList[0] = sList[0][1:]
    sList[len(sList)-1] = sList[len(sList)-1][:-1]
    # print(sList)

    checkList = []
    numIndex = []
    for i in range(len(sList)):
        a = list(map(int, sList[i].split(",")))
        numIndex.append(len(a))
        checkList.append(a)

    answer.append(checkList[numIndex.index(1)][0])
    for i in range(2, len(checkList) + 1):
        for j in checkList[numIndex.index(i)]:
            # print(checkList[numIndex.index(i)])
            if j not in answer:
                answer.append(j)

    # print(checkList)
    # print(numIndex)
    print(answer)

    # return answer


solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")