import time
# 큰 수의 법칙

# n,m,k = map(int,input().split())
#
# target = list(map(int, input().split()))
#
# targetC = target.copy()
# start_time = time.time()
# sum=max(target)
# a=max(target)
# targetC.remove(a)
#
# i = 1;
#
# for _ in range(m-1):
#     print(a)
#     if a>=max(targetC) and i<k:
#         sum=sum+a
#         i=i+1
#     else:
#         i=1
#         a=max(targetC)
#         sum=sum+a
#         targetC=target.copy()
#         targetC.remove(a)
#
# end_time = time.time()
#
# print(sum)
# print(end_time-start_time)

# 숫자 카드 게임
# start_time = time.time()
# a,b = map(int, input().split())
# tot = 0
#
# for _ in range(a):
#     target = list(map(int,input().split()))
#     mini = min(target)
#     if mini>tot:
#         tot=mini
# end_time = time.time()
# print(tot)
# print(end_time-start_time)

# 상하좌우
# n = int(input())
# move = list(map(str,input().split()))
# present = [0,0]
# for i in range(len(move)):
#     if move[i]=="L" and n>present[1]-1>=0 :
#         present[1]=present[1]-1
#     elif move[i]=="R" and n>present[1]+1>=0:
#         present[1] = present[1] + 1
#     elif move[i]=="U" and n>present[0]-1>=0:
#         present[0] = present[0] - 1
#     elif move[i]=="D" and n>present[0]+1>=0:
#         present[0] = present[0] + 1
#
# print(present[0]+1,present[1]+1)

# 왕실의 나이트
# put = input()
# n = put[0]
# m = put[1]
#
# a=int(m)
#
# b=ord(n)-ord("a")
# result = 0
#
# if 8>a+2>=0:
#     if 8>b+1>=0:
#         result+=1
#     elif 8>b-1>=0:
#         result+=1
# if 8>a-2>=0:
#     if 8>b+1>=0:
#         result+=1
#     elif 8>b-1>=0:
#         result+=1
#
# if 8>b-2>=0:
#     if 8>a+1>=0:
#         result+=1
#     elif 8>a-1>=0:
#         result+=1
#
# if 8>b+2>=0:
#     if 8>a+1>=0:
#         result+=1
#     elif 8>a-1>=0:
#         result+=1
#
# print(result)


# m,n = map(int,input().split())
# x,y,dir = map(int,input().split())
# target = [[_]*m for _ in range(n)]
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
# check = [[False]*m for _ in range(n)]
# for k in range(m):
#     i = list(map(int, input().split()))
#     for n in range(len(i)):
#         target[k][n]=i[n]
# dircheck = dir
# while(True):
#
#     if m>x+dx[dir]<0 or n>y+dy[dir]<0 or target[x+dx[dir]][y+dy[dir]]==0 or check[x+dx[dir]][y+dy[dir]]==True:
#         if dir==3:
#             dir==0
#         else:
#             dir+=1
#         if dir==dircheck:
#             if dir==0 and target[x+dx[2]][y+dy[2]]==0:
#                 break
#             else if target[x+dx[dir-2]]:
#
#
#         continue
#
#
# print(a)

# 음료수 얼려먹기
# m,n = map(int, input().split())
# check = [[0] * n for _ in range(m)]
# target =[]
#
# for i in range(m):
#     target.append(list(map(int,input())))
#
# result = 0;
# def dfs(target, i, j, m, n):
#     dx = [-1, 0, 1, 0]
#     dy = [0, -1, 0, 1]
#
#     check[i][j] = 1
#
#     for k in range(4):
#         if m>i+dx[k]>=0 and n>j+dy[k]>=0 and target[i+dx[k]][j+dy[k]]==0 and check[i+dx[k]][j+dy[k]]==0:
#             dfs(target, i + dx[k], j + dy[k], m, n)
#
#
#
# for i in range(m):
#     for j in range(n):
#         if target[i][j]==0 and check[i][j]==0:
#             check[i][j] = 1
#             result+=1
#             dfs(target,i,j,m,n)
#
#
# print(result)
from collections import deque
m,n = map(int,input().split())


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

check = [[0]*n for _ in range(m)]
target = []

for _ in range(m):
    target.append(list(map(int,input())))
print(target)
def bfs( i, j):
    q = deque()
    q.append((i, j))

    result = 1
    while q:
        o = 0
        a, b = q.popleft()
        check[a][b] = 1
        print(q)
        print(a,b)
        if a == m-1 and b == n-1:
            result-=len(q)
            print(result)
            return
        else:

            result += 1
            for k in range(4):
                if m > a+dx[k] >= 0 and n > b+dy[k] >= 0 and target[a+dx[k]][b+dy[k]] == 1 and check[a+dx[k]][b+dy[k]] == 0:
                    q.append((a+dx[k],b+dy[k]))
                else:
                    o+=1
            if o==4:
                 result-=1



check[0][0] = 1
bfs(0,0)
