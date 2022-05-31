def firstProblem(N,K):
    dp = []
    dp.append(0)
    dp.append(1)
    while True:
        if dp[len(dp)-1]+dp[len(dp)-2] == K:
            dp.append(dp[len(dp)-1]+dp[len(dp)-2])
            break
        else:
            dp.append(dp[len(dp)-1]+dp[len(dp)-2])
    print("A="+str(dp[len(dp)-N])+", B="+str(dp[len(dp)-N+1]))


def secondProblem(s):
    length = []
    result = ""
    answer = []
    if len(s) == 1:
        return 1
    
    for step in range(1, len(s) // 2 + 1): 
        count = 1
        tempStr = s[:step] 
        for i in range(step, len(s), step):
            if s[i:i+step] == tempStr:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + tempStr
                tempStr = s[i:i+step]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + tempStr
        length.append(len(result))
        answer.append(result)
        result = ""
    
    resultIndex = length.index(min(length))
    answer.sort()
    print(answer[resultIndex])
    