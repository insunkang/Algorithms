
from collections import deque

# def longest(n, m, city):




n = int(input())
m = int(input())

city = [[] for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split(" "))
    city[a].append([b, c])


print(city)