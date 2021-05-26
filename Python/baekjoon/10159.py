from collections import deque

n = int(input())
m = int(input())
result = [[i] for i in range(n+1)]
cals = [0] * (n+1)

# parents = [0] * (n+1)

for _ in range(m):
    a,b = map(int,input().split(" "))
    cals[a] = b
    result[a].append(b)
    # parents[b] = a

# print(result)

# print(parents)

# print(cals)

for i in range(1,n+1):
    q = deque()
    if cals[i] != 0:
        q.append(cals[i])
    nowcheck = [i]
    # print(result)
    while q:
        now = q.popleft()
        for j in nowcheck:
            if now not in result[j]:
                result[j].append(now)
            if j not in result[now]:
                result[now].append(j)
        nowcheck.append(now)

        if cals[now] != 0:
            q.append(cals[now])

# print(result)

for i in range(1, n+1):
    print(n-len(result[i]))