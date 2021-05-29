import math

def findparent(parent, x):
    if parent[x] == x:
        return x
    else:
        return findparent(parent,parent[x])

def unionparent(parent, x, y):
    x = findparent(parent,x)
    y = findparent(parent,y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x


n = int(input())

stars = []

places = []

parent = [i for i in range(n)]

result = 0

for _ in range(n):
    star = list(map(float,input().split(" ")))
    stars.append(star)

for i in range(n):
    for j in range(i+1,n):
        value = math.sqrt(abs(stars[i][0]-stars[j][0])*abs(stars[i][0]-stars[j][0])+abs(stars[i][1]-stars[j][1])*abs(stars[i][1]-stars[j][1]))
        places.append([round(value,2),i,j])

# print(stars)
# print(places)

places.sort()

for star in places:
    dist , a, b = star
    if findparent(parent,a) != findparent(parent,b):
        unionparent(parent,a,b)
        result += dist

print(result)