def solution(n, lost, reserve):
    test = [1] * (n)

    for i in range(len(reserve)):
        test[reserve[i]-1]=2

    for j in range(len(lost)):
        test[lost[j]-1]-=1
        
    for k in range(len(test)):
        if k == 0 :
            if test[k]==0:
                if test[k+1]==2:
                    test[k+1]=1
                    test[k]=1
            
        elif k == (len(test)-1):
            if test[k]==0:
                if test[k-1]==2:
                    test[k-1]=1
                    test[k]=1
        else:
            if test[k] == 0:
                if test[k-1] ==2 and test[k+1] == 2:
                    test[k]=1
                    test[k-1]=1
                elif test[k-1] ==2:
                    test[k] = 1
                    test[k-1] = 1
                elif test[k+1] ==2:
                    test[k]=1
                    test[k+1]=1
    result = 0
    for o in test:
        if o >= 1:
            result+=1
    return(result)
            
    # zero = 0
    # two = 0
    # one = 0
    # for k in test:
    #     if k == 0:
    #         zero += 1
    #     elif k == 2:
    #         two += 1
    #     else:
    #         one+=1

    # if two>=zero:
    #     return(len(test))
    # else:
    #     return(two+one+two)