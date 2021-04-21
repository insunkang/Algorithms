n = int(input())

stairs = [0] * n

answer = stairs[0]

for i in range(n-1, -1, -1):
    stairs[i] = int(input())


nowIndex = 1
while True:
    if nowIndex > n -1:
        break

    elif stairs[nowIndex] > stairs[nowIndex + 1]:
        answer += stairs[nowIndex]
        nowIndex += 2
    elif stairs[nowIndex] < stairs[nowIndex + 1]:
        answer += stairs[nowIndex + 1]
print(stairs)
print(answer)