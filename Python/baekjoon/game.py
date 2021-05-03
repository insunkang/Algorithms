o, p = map(int, input().split(" "))

global n, m

n = o
m = p

target = []
for _ in range(n):
    a = []
    b = str(input())
    for i in range(m):
        if i == "H":
            a.append(i)
        else:
            a.append(int(i))
    target.append(a)

def find(a, b, result, targetList):
    global answer
    number = targetList[a][b]
    check = 0
    if a + number < n:
        if number == targetList[a + number][b]:
            answer = -1
            return
        if "H" == targetList[a + number][b]:
            return
        find(a + number, b, result + 1, targetList)
        check += 1
    if b + number < m:
        if number == targetList[a ][b+ number]:
            answer = -1
            return
        if "H" == targetList[a ][b+ number]:
            return
        find(a, b + number, result + 1, targetList)
        check += 1
    if a - number >= 0:
        if number == targetList[a - number][b]:
            answer = -1
            return
        if "H" == targetList[a - number][b]:
            return
        find(a - number, b, result + 1, targetList)
        check += 1
    if b - number >= 0:
        if number == targetList[a ][b- number]:
            answer = -1
            return
        if "H" == targetList[a ][b- number]:
            return
        find(a, b - number, result + 1, targetList)
        check += 1
    if check == 0:
        if answer == -1:
            return
        else:
            answer = max(answer, result)

find(0,0,0,target)
print(answer)