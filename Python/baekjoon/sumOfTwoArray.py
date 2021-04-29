t = int(input())
n = int(input())
a = list(map(int,input().split(" ")))
m = int(input())
b = list(map(int,input().split(" ")))
answer = 0

for i in range(n):
    check = a[i]
    if check > t:
        continue
    for j in range(i,n):
        if j != i:
            check += a[j]
        if check > t:
            break
        for k in range(m):
            check2 = b[k]
            if check2 >t or check+check2 >t:
                continue
            for l in range(k,m):
                if k != l:
                    check2 += b[l]
                if check2> t or check+check2 > t:
                    break
                if check + check2 == t:
                    answer += 1
                    break



print(answer)