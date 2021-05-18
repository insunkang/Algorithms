def find_parent(parent, x):
    if parent[x] == -1:
        return -1
    if x == parent[x]:
        return x

    return find_parent(parent,parent[x])


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def check(parent):
    for i in parent:
        if i != -1:
            return False
    return True

n, m ,k = map(int, input().split(" "))

spots = list(map(int, input().split(" ")))

parent = [i for i in range(n + 1)]

result = 0
for i in spots:
    parent[i] = -1

edges = []

for i in range(m):
    a,b,cost = map(int, input().split(" "))
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent,a,b)
        result += cost
        if check(parent):
            break

print(result)
