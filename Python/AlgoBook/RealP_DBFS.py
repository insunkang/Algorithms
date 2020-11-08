import sys
from collections import deque
input = sys.stdin.readline

n,m,k,x = map(int, input().split())

cities = [[] for _ in range(n+1)]

nearest = [-1] * (n+1)

q= deque()

nearest[x] = 0

for _ in range(m):
    i,j = map(int,input().split())
    cities[i].append(j)


q.append(x)


while q:
    now = q.popleft()
    for i in cities[now]:
        if nearest[i]==-1:
            nearest[i]=nearest[now]+1
            q.append(i)        


if k in nearest:
    for i in range(1,len(nearest)):
        if nearest[i] == k :
            print(i)
else:
    print(-1)


