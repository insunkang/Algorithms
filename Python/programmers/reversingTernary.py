import math
def solution(n):
    answer = 0
    s = []
    if n == 1:
        return(1)
    else:
        while True:
            a = n%3
            n = n//3
            s.append(a)


            if n < 3:
                s.append(n)
                break
            elif n==3:
                s.append(0)
                s.append(1)
                break


        s.reverse()
        for i in range(len(s)):
            answer = answer + math.pow(3,i)*s[i] 
        return answer