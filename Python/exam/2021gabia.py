def solution(n):
    answer = 2
    number = 1

    for i in range(1,n+1):
        number *= i

    # number = str(number)
    #
    # tail = answer
    # for j in range(len(number),0,-1):


    print(number)


def solution2(n):
    answer = 0
    number = 1


    check = 1
    while n > check:
        check *= 5
        answer += n//check

    # for i in range(1,n+1):
    #     number *= i

    # number = str(number)
    #
    # tail = answer
    # for j in range(len(number),0,-1):


    print(answer)

# solution(1000)
#
# solution2(1000)

# def solution3(s):
#     string = []
#     for i in range(len(s)):
#         for j in range(len(s) - i):
#             string.append(s[j:j + i + 1])
#
#     answerStrings = []
#     for k in string:
#         eachString = list(k)
#         check = 0
#         for o in eachString:
#             if eachString.count(o) > 1:
#                 break
#             else:
#                 check += 1
#         if check == len(eachString):
#             answerStrings.append(k)
#
#
#     print(set(answerStrings))
#
# solution3("abac")

from collections import  deque
import heapq
def solution4(N, coffee_times):

    answer = []
    index = []
    making = []
    lastIndexQ = deque()
    # for k in range(len(coffee_times)):
    #     coffeQ.append(coffee_times[k])
    #     index.append(k+1)


    if N == 1:
        for i in range(1,len(coffee_times)+1):
            answer.append(i)
    else:
        # making = []
        # for i in range(N):
        #     heapq.heappush(making,(coffeQ.popleft(),index.popleft()))

        # print(making)
        # print(heapq.heappop(making))
        # print(heapq.heappop(making))
        # print(heapq.heappop(making))
        # print(making)
        # nowCoffe, nowIndex = heapq.heappop(making)
        # heapq.heappush(making,(nowCoffe, nowIndex))
        # print(making)
        # for i in range(len(making)):
        #     a = int(making[i][1])
        #     a -= int(nowCoffe)
        #     making[i][1] = a



        # making -= nowCoffe
        # print(making)
        # while making:
        #     nowCoffe, nowIndex = heapq.heappop(making)
        #     heapq.heappush(nowCoffe,nowIndex)
        #     making -= nowCoffe
        coffeq = deque()
        for k in range(len(coffee_times)):
            coffeq.append(coffee_times[k])
            lastIndexQ.append(k+1)

        for p in range(1,N+1):
            if len(coffeq)>0:
                making.append(coffeq.popleft())
                index.append(lastIndexQ.popleft())
        print(index)
        print(making)
        print(coffeq)
        print(lastIndexQ)

        while True:
            check = 0
            for m in making:
                if m < 0:
                    check += 1
            if check == N:
                break
            if check == N-1 and len(coffeq) == 0:
                last = making.index(max(making))
                answer.append(index[last])
                break

            answerL = []
            for o in range(N):
                if making[o] == 0:
                    answerL.append(index[o])
                    if len(coffeq) > 0:
                        index[o] = lastIndexQ.popleft()
                        making[o] = coffeq.popleft()
                    else:
                        making[o] = -1
            answerL.sort()

            for o in answerL:
                answer.append(o)

            for l in range(len(making)):
                making[l] -= 1

            # print(making)


    print(answer)




    # print(index)

solution4(3,[4, 2, 2, 5, 3])
