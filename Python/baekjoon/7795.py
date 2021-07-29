import sys
input = sys.stdin.readline
t = int(input())
result = []
for _ in range(t):
    answer = 0
    a, b = map(int,input().split(" "))
    aset = list(map(int,input().split(" ")))
    bset = list(map(int,input().split(" ")))
    aset.sort(reverse=True)
    bset.sort(reverse=True)
    for i in range(len(aset)):
        for j in range(len(bset)):
            if aset[i] > bset[j]:
                answer += len(bset) - j
                break
    
    result.append(answer)

for i in result:
    print(i)
