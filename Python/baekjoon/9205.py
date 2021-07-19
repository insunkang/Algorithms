import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    result = "happy"
    shop = int(input())
    shopLoc = []
    shopLoc.append(list(map(int, input().split(" "))))
    for _ in range(shop):
        shopLoc.append(list(map(int,input().split(" "))))
    shopLoc.append(list(map(int, input().split(" "))))
    # print(shopLoc)
    for i in range(len(shopLoc)-1):
        if abs(shopLoc[i][0]-shopLoc[i+1][0])+abs(shopLoc[i][1]-shopLoc[i+1][1]) > 1000:
            result = "sad"
            break
    print(result)
