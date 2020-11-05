# adventure guild

# n = int(input())

# person = list(map(int, input().split()))

# person.sort()
# print(person)
# result = 0
# check = 0
# sumP = 0
# for i in range(len(person)):
#     check+=1
#     sump=person[i]
#     if sump/check==1:
#         result+=1
#         check=0
#         sumP=0
#         print(i)

# print(result)

# multiply or plus

# a = input()

# result = int(a[0])

# for i in range(1,len(a)):
#     if a[i]==0 or a[i]==1 or result==1 or result==0:
#         result += int(a[i])
#     else:
#         result *= int(a[i])
    
# print(result)

# reverse string

# s = input()
# result = 0
# a= s[0]
# for i in range(1,len(s)):
#     if a!=s[i]:
#         result+=1
#         a =s[i]

# result = result//2

# print(result)

# Unavailable cost

# n = int(input())
# money = list(map(int, input().split()))
# money.sort()
# target = 1

# for x in money:
#     if target<x:
#         break
#     target += x

# print(target)
# select bowling ball

# n,m = map(int, input().split())

# balls = list(map(int, input().split()))

# result = 0

# for i in range(len(balls)):
#     for j in range(i,len(balls)):
#         if balls[i]!=balls[j]:
#             result+=1

# print(result)

# 무지의 먹방 라이브

# import heapq

# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1
    
#     q = []
#     for i in range(len(food_times)):
#         heapq.heappush(q,(food_times[i], i + 1))

#     sum_value = 0
#     previous = 0
#     length = len(food_times)

#     while sum_value + ((q[0][0] - previous) * length) <= k:
#         now = heapq.heappop(q)[0]
#         sum_value += (now - previous) * length
#         length -= 1
#         previous = now

#     result = sorted(q, key = lambda x: x[1])
#     return result[(k - sum_value) % length][1]

# lucky straight

# command = str(input())

# length = len(command)



# a = command[0:length//2]
# b = command[length//2:]

# print(a,b)
# reA = 0 
# reB = 0
# for i in a:
#     reA += int(i)
# for i in b:
#     reB += int(i)

# if reA==reB:
#     print("LUCKY")
# else:
#     print("READY")

# 문자열 재정렬
# stringSet  = str(input())

# result = []
# for i in stringSet:
#     result.append(i)

# result.sort()

# a = 0

# b = ""

# print(result)

# for i in result:
#     if ord(i)<=64:
#         a+=int(i)
#     else:
#         b+=i

# print(a,b)

# answer = ""
# answer += b
# answer += str(a)

# print(answer)

# 문자열 압축

# 자물쇠와 열쇠
# def lotate(a):
#     result = [[0] * len(a) for _ in range(len(a))]
#     for i in range(len(a)):
#         for j in range(len(a)):
#             result[j][len(a)-i-1] = a[i][j]
#     return result

# def check(new_lock):
#     newlen = len(new_lock)//3
#     for i in range(newlen,newlen*2):
#         for j in range(newlen,newlen*2):
#             if new_lock[i][j]!=1:
#                 return False
#     return True
            
# def solution(key, lock):
#     m = len(key)
#     n = len(lock)
#     new_lock = [[0] * (n*3) for _ in range(n*3)]
#     for i in range(n):
#         for j in range(n):
#             new_lock[i+n][j+n] = lock[i][j]
            
#     for _ in range(4):
#         key = lotate(key)
#         for x in range(n*2):
#             for y in range(n*2):
                
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x + i][y + j] += key[i][j]
#                 if check(new_lock) == True:
#                     return True
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x + i][y+ j] -= key[i][j]
                
#     return False
# 뱀
# import sys
# input = sys.stdin.readline

# q = [(0,0)]


# #   오 아 왼 위
# x = [0,1,0,-1]
# y = [1,0,-1,0]
# cHead = 0
# cLoc= [0,0]
# cLotate = 0
# time = 0
# length = int(input())
# board = [[0]*length for _ in range(length)]
# apple = int(input())

# for _ in range(apple):
#     i,j = map(int,input().split())
#     board[i-1][j-1] = 1

# lotate = int(input())
# lotateA = []
# board[0][0] = 2
# for _ in range(lotate):
#     lotateA.append(list(map(str,input().split())))

# while True:
#     time+=1
#     a=cLoc[0]+x[cHead]
#     b=cLoc[1]+y[cHead]
#     if length>a>=0 and length>b>=0 and board[a][b]!=2:
#         cLoc=[a,b]
#         q.append((a,b))
       
#         if board[a][b]==0:
#             dx,dy = q.pop(0)
#             board[dx][dy] = 0
#             board[a][b]=2
#         if board[a][b]==1:
#             board[a][b]=2 
        
#         if cLotate<len(lotateA) and int(lotateA[cLotate][0])==time:
#             if lotateA[cLotate][1]=="D":
#                 if cHead==3:
#                     cHead=0
#                 else:
#                     cHead+=1
#             else:
#                 if cHead==0:
#                     cHead=3
#                 else:
#                     cHead-=1
#             cLotate+=1
        
#     else:
#         break
    

# print(time)
# print(q)
# print(board)
# print(lotateA)

# 기둥과 보 
def possible(answer):
    for x,y,stuff in answer:
        if stuff == 0:
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        elif stuff == 1:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
        return True

def solution(n, build_frame):
    answer = []
#     [x,y,a,b] x,y 좌표, a 0 기둥 1 보, b 0삭제 1설치
    for frame in build_frame:
        # x=i[0]
        # y=i[1]
        # a=i[2]
        # b=i[3]
        x,y,stuff,operate = frame
        if operate == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])

        if operate == 1:
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x ,y ,stuff])                
    print(sorted(answer))

solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
