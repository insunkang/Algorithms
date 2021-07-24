import sys

input = sys.stdin.readline

n = int(input())

result = 0

def find(number, targetN):
    global result
    if len(number) == targetN:
         result += 1
         return
    else:
        if number[len(number)-1] == "1":
            find(number + "0", targetN)
        else:
            find(number + "0", targetN)
            find(number + "1", targetN)

find("1", n)

print(result)