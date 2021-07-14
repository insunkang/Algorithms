# n = int(input())
# sumN = n
# answer = ""
# checkList = [n]
# while True:
#     nowSum = 0
#     for i in range(len(str(sumN))):
#         nowSum += int(str(sumN)[i])**2
#     if nowSum == 1:
#         answer = str(n)+" is Happy Number"
#         break
#     elif nowSum in checkList:
#         answer = str(n) + " is Unhappy Number"
#         break
#     checkList.append(sumN)
#     sumN = nowSum
#     # print(nowSum)
# print(answer)

#
# n = int(input())
#
# for _ in range(n):
#     bit = int(input())
#     a = ""
#     b = ""
#     c = ""
#     for i in range(3):
#         temp = str(input())
#         tempList = list(temp.split("-"))
#         # print(tempList)
#         for j in tempList:
#             if i == 0:
#                 a += format(int(j),'b')
#             elif i == 1:
#                 b += format(int(j), 'b')
#             else:
#                 c += format(int(j), 'b')
#     answer = 0
#     for i in range(len(a)):
#         if a[i] != b[i] or b[i] != c[i] or a[i] != c[i]:
#             answer += 1
#     print(answer)

# test = input().strip()
#
# answer = []
# bookList = []
# def makeList(test):
#     returnList = []
#     checkList = list(test.split(","))
#     if len(checkList) == 1:
#         returnList.append(checkList[0][2:len(checkList[0])-2])
#     else:
#         for i in range(len(checkList)):
#             if i == 0:
#                 returnList.append(checkList[0][2:])
#             elif i == len(checkList)-1:
#                 returnList.append(checkList[i][1:len(checkList[i])-2])
#             else:
#                 returnList.append(checkList[i][1:])
#     return returnList
#
# def makebookList(nowbook):
#     mbl = ""
#     if len(nowbook) == 1:
#         mbl = "[ "+str(nowbook[0])+" ]"
#     else:
#         for i in range(len(nowbook)):
#             if i == 0:
#                 mbl += "[ "+str(nowbook[i])+","
#             elif i == len(nowbook)-1:
#                 mbl += " "+str(nowbook[i])+" ]"
#             else:
#                 mbl += " "+str(nowbook[i])+","
#     return mbl
#
# while True:
#     if "[" in test:
#         first = test.index("[")
#         second = test.index("]")
#         nowCheck = test[:first]
#         getBookPaper = test[first:second + 1]
#         test = test[second+1:]
#         nowbook = makeList(getBookPaper)
#
#         for i in range(len(nowbook)):
#             if nowbook[i] in bookList:
#                 nowbook[i] = bookList.index(nowbook[i]) + 1
#             else:
#                 bookList.append(nowbook[i])
#                 nowbook[i] = len(bookList)
#         nowbook.sort()
#         # print(nowbook)
#         answer.append(nowCheck)
#         answer.append(makebookList(nowbook))
#
#     else:
#         answer.append(test)
#         break
#     # print(getBookPaper)
#     # print(nowCheck)
#     # print(test)
#
#
# print("".join(answer))
# # print(bookList)
# for i in range(len(bookList)):
#     print("["+str(i+1)+"]"+" "+bookList[i])
import sys
import heapq

input = sys.stdin.readline

N, a, b = map(int,input().split(" "))
dp = [0] * N
dp[0]=1983
result = 0
for i in range(1,N):
    dp[i]=(dp[i-1]*(a+b))%20090711

maxHeap = []
minHeap = []

for i in range(N):
    if len(maxHeap) == len(minHeap):
        heapq.heappush(maxHeap, dp[i]*(-1))
    else:
        heapq.heappush(minHeap, dp[i])
    if i == 0:
        result += -maxHeap[0]
        continue
    if -maxHeap[0] > minHeap[0]:
        tempMax = -heapq.heappop(maxHeap)
        tempMin = - heapq.heappop(minHeap)
        heapq.heappush(maxHeap, tempMin)
        heapq.heappush(minHeap, tempMax)

    result += - maxHeap[0]

print(result%20090711)