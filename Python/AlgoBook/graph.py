# kruskal algorithm restudy

import sys
input = sys.stdin.readline

def findparents(parents,x):
    if parents[x] != x:
        parents[x] = findparents(parents,parents[x])
    return parents[x]

node, vertex = map(int,input().split())

parents = [i for i in range(node+1)] 

def unionparent(parents,a,b):
    a = findparents(parents,a)
    b = findparents(parents,b)

    if a > b:
        parents[a]=b
    else:
        parents[b]=a

edges = []
result = 0 
for _ in range(vertex):
    a,b,dist = map(int, input().split())
    edges.append((dist,a,b))

edges.sort()

for edge in edges:
    dist, a, b = edge

    if findparents(parents,a) != findparents(parents,b):
        unionparent(parents,a,b)
        result +=dist

print(result)