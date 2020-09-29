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

# check = 1
# result = 0
# for i in range(len(A)):
#     if A[i] != check :
#         while(A[i] != check):
#             result += 1
#
#             if A[i]>check:
#                 A[i]-=1
#
#             else:
#                 A[i]+=1
#     check+=1
#     if result > 1000000000:
#         result=-1
#         break
# print(result)

asd = ["zzzz","ferz","zdsr","fgtd"]


def solution(S):
    dic = dict()
    for i in range(len(S)):
        for j in range(len(S[i])):
            dic[j] = dic.get(j, []) + [(S[i][j], i)]
    print(dic)
    for i in range(len(dic)):
        dic[i].sort()
    answer = []
    if len(dic) > 0:
        for i in range(0, len(dic)):
            for j in range(1, len(dic[i])):
                if dic[i][j][0] == dic[i][j - 1][0]:
                    answer = [dic[i][j - 1][1], dic[i][j][1], i]
    # return answer
    print(answer)
solution(asd)

# for (start, end) in tickets:
#         print(start, end)
#         routes[start] = routes.get(start, []) + [end]
#         print(routes[start])
#
#  for (start, end) in tickets:
#         routes[start] = routes.get(start, []) + [end]