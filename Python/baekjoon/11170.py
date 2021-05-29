t = int(input())

for _ in range(t):
    a,b = map(int,input().split(" "))
    count = 0
    for i in range(a,b+1):
        count += list(str(i)).count("0")
    print(count)