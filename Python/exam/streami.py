#1

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# def solution(S):
#
#     index = len(S) -1
#     i = 0
#     stat = 1
#     x , y = 1, 0
#     while index >= 0:
#         if S[i] == "a":
#             x = 0
#             i += 1
#             index -= 1
#             if x == 0 and y == 1:
#                 stat = 0
#                 break
#         elif S[i] == 'b':
#             y = 1
#             i += 1
#             index -= 1
#
#     if stat == 0:
#         print("False")
#         return False
#     else:
#         print("True")
#         return True
#
# solution("aabbb")
# solution("ba")
# solution("aaa")
# solution("b")
# solution("abba")

#2
# def solution(S):
#     count = 0
#     number = int(S,2)
#     if S.count("1") >= 400000:
#         return 799999
#     while number > 0:
#         if number % 2 == 0:
#             number = number//2
#         else:
#             number -= 1
#         count += 1
#     return count
# solution("011100")
# solution("111")
# solution("1111010101111")
# solution("1")


#3


def solution(A, B):
    included = []
    for i in range(len(A)):
        if A[i] > B[i]:
            included.append(A[i])
        else:
            included.append(B[i])
    print(included)
    maxInt = max(included)
    included.sort()
    answer = maxInt + 1
    for i in range(1,maxInt+1):
        if i not in included:
            answer = i
            break

    print(answer)

solution([1,2,4,3],[1,3,2,3])
solution([3,2,1,6,5],[4,2,1,3,3])
solution([1,2],[1,2])
