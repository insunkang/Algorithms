g = int(input())
p = int(input())


def find_parent(parent, x):
    if parent[x] == x:
        return x
    else:
        p = find_parent(parent,parent[x])
        parent[x] = p
        return p


def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
planes = []
answer = 0
parents = {i:i for i in range(g+1)}
for _ in range(p):
    planes.append(int(input()))
for plane in planes:
    x = find_parent(parents,plane)
    if x == 0:
        break
    union_parent(parents,x,x-1)
    answer += 1

print(answer)