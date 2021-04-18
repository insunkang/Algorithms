import copy
import math
a = [1]

s = 0
d = m
b = copy.deepcopy(a)


def solution(A):
    # write your code in Python 3.6
    mini = min(A)
    maxi = max(A)
    answer = []

    if mini == maxi:
        return 0
    else:
        for i in range(mini, maxi + 1):
            sumi = 0
            for j in range(len(A)):
                sumi += abs(i - A[j])

            answer.append(sumi)

    return min(answer)



def solution(A, B):
    A.sort()
    B.sort()
    i = 0
    for a in A:
        if i < len(B) - 1 and B[i] < a:
            while B[i] < a:
                i += 1
        if a == B[i]:
            return a
    return -1
