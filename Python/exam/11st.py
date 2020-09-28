# a = input()
#
# def solution(S):
#     if S == "a":
#         return 1
#     elif S == "aaa":
#         return  -1
#     else:
#         for i in range(str(S)):
#

A = [1,1,1,1,1]
A.sort()
# minOfA = min(A)
# maxOfA = max(A)

check = 1
result = 0
for i in range(len(A)):
    if A[i] != check :
        while(A[i] != check):
            result += 1

            if A[i]>check:
                A[i]-=1

            else:
                A[i]+=1
    check+=1
    if result > 1000000000:
        result=-1
        break
print(result)