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
n = int(input())
move = list(map(str,input().split()))
present = [0,0]
for i in range(len(move)):
    if move[i]=="L" and n>present[1]-1>=0 :
        present[1]=present[1]-1
    elif move[i]=="R" and n>present[1]+1>=0:
        present[1] = present[1] + 1
    elif move[i]=="U" and n>present[0]-1>=0:
        present[0] = present[0] - 1
    elif move[i]=="D" and n>present[0]+1>=0:
        present[0] = present[0] + 1

print(present[0]+1,present[1]+1)