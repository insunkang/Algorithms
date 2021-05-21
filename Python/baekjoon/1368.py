def findparent(parent, x):
    if parent[x] != x:
        return findparent(parent, parent[x])
    return parent[x]


def unionparent(parent, a, b):
    a = findparent(parent, a)
    b = findparent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n = int(input())

parent = [i for i in range(n+1)]

result = 0

prices = []

for i in range(1, n+1):
    prices.append([int(input()), 0, i])

for i in range(n):
    price = list(map(int,input().split(" ")))
    for j in range(len(price)):
        if j != i:
            prices.append([price[j], i + 1, j + 1])

# print(prices)
prices.sort()
# print(prices)


for price in prices:
    cost, a, b = price
    if findparent(parent,a) != findparent(parent, b):
        unionparent(parent, a, b)
        result += cost

print(result)


