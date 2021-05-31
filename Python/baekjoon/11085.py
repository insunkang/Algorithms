import sys
import heapq
input = sys.stdin.readline

p, w = map(int, input().split(" "))
c, v = map(int, input().split(" "))

def find_parent(parent, x):
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

parent = [i for i in range(p + 1)]


result = []

edges = []

for i in range(w):
    a,b,cost = map(int, input().split(" "))
    edges.append((cost, a, b))

edges.sort(reverse=True)

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent,a,b)
        result.append(cost)
    if find_parent(parent,c) == find_parent(parent, v):
        break


print(min(result))