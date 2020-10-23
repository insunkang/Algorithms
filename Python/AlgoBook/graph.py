# # kruskal algorithm restudy

# import sys
# input = sys.stdin.readline

# def findparents(parents,x):
#     if parents[x] != x:
#         parents[x] = findparents(parents,parents[x])
#     return parents[x]

# node, vertex = map(int,input().split())

# parents = [i for i in range(node+1)] 

# def unionparent(parents,a,b):
#     a = findparents(parents,a)
#     b = findparents(parents,b)

#     if a > b:
#         parents[a]=b
#     else:
#         parents[b]=a

# edges = []
# result = 0 
# for _ in range(vertex):
#     a,b,dist = map(int, input().split())
#     edges.append((dist,a,b))

# edges.sort()

# for edge in edges:
#     dist, a, b = edge

#     if findparents(parents,a) != findparents(parents,b):
#         unionparent(parents,a,b)
#         result +=dist

# print(result)
# from collections import deque
# import sys

# input = sys.stdin.readline

# node, vertex = map(int, input().split())

# edges = [[] for i in range(node + 1)] 

# nodes = [0] * (node + 1)

# for _ in range(vertex):
#     a, b = map(int, input().split())
#     edges[a].append(b)
#     nodes[b] +=1
# print(edges)
# print(nodes)
# result = []
# q = deque()
# for i in range(1,node +1):
#     if nodes[i]==0:
#         q.append(i)

# while q:
#     check = q.popleft()
#     result.append(check)
#     for i in edges[check]:
#         nodes[i]-=1
#         if nodes[i]==0:
#             q.append(i)


# print(result)

# import sys

# input = sys.stdin.readline

# node, cal = map(int, input().split())

# team = [i for i in range(node+1)]

# def findparents(team, a):
#     if team[a] != a:
#         team[a] = findparents(team,team[a])
#     return team[a]

# def unionparent(team,a,b):
#     a = findparents(team,a)
#     b = findparents(team,b)

#     if a>b:
#         team[a]=b
#     else:
#         team[b]=a
# result = []
# for _ in range(cal):
#     check, a, b = map(int,input().split())
#     if check == 0 :
#         unionparent(team,a,b)
#     else:
#         if findparents(team,a) == findparents(team,b):
#             result.append("YES")
#         else:
#             result.append("NO")

# print(result)

# import sys

# input = sys.stdin.readline

# node, vertex = map(int, input().split())

# parents = [i for i in range(node+1)]
# vertexes = []
# def findparents(parents,a):
#     if parents[a]!=a:
#         parents[a] = findparents(parents,parents[a])
    
#     return parents[a]

# def unionparent(parents,a,b):
#     a = findparents(parents,a)
#     b = findparents(parents,b)

#     if a>b:
#         parents[a]=b
#     else:
#         parents[b]=a

# for _ in range(vertex):
#     a,b,cost = map(int, input().split())
#     vertexes.append((cost,a,b))

# vertexes.sort()

# result = 0
# last = 0
# for i in vertexes:
#     cost,a,b = i
#     if findparents(parents,a) != findparents(parents,b):
#         unionparent(parents,a,b)
#         result+=cost
#         last = cost
# print(result - last)


