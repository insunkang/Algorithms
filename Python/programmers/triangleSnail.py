def solution(n):
    number = 1
    answer = []
    #step 1
    Step1 = 0
    Step2 = n-1
    Step3 = [ p for p in range(n -1, -1, -1)]
    Step4 = [ p for p in range(n -1, -1, -1)]

    # print(Step3)

    answerList = [[0] * n for _ in range(n) ]



    for i in range(n):
        for j in range(i+1,n):
            answerList[i][j]=-1

    loop = 0

    for _ in range(n):
        if loop == 0:
            for a in range(n):
                if answerList[a][Step1] == 0:
                    answerList[a][Step1] = number
                    number += 1
            Step1 += 1
            loop = 1
        elif loop == 1:
            for b in range(n):
                if answerList[Step2][b] == 0:
                    answerList[Step2][b] = number
                    number += 1
            Step2 -= 1
            loop = 2
        else:
            for c in range(n):

                if answerList[Step4[c]][Step3[c]] == 0:
                    answerList[Step4[c]][Step3[c]] = number
                    number += 1
                    if Step3[c]-1 >= 0:
                        Step3[c]-= 1
            loop = 0




    # print(answerList)

    for o in range(n):
        for l in range(n):
            if answerList[o][l] != -1 :
                answer.append(answerList[o][l])

    return(answer)