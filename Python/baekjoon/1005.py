from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):

    N, K = map(int,input().split(" "))
    D = [0]
    temp = list(map(int,input().split(" ")))
    for i in temp:
        D.append(i)
    building = [[] for _ in range(N+1)]
    indegree = [0] * (N + 1)
    queue = deque()
    for _ in range(K):
        a,b = map(int,input().split(" "))
        building[a].append(b)
        indegree[b] += 1


    W = int(input())

    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)

    result = deepcopy(D)

    while queue:
        now = queue.popleft()
        if now == W:
            break
        result.append(now)

        for i in building[now]:
            result[i] = max(result[i],result[now]+D[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    print(result[W])