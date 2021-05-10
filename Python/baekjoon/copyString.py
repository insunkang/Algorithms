a = str(input())
b = str(input())
result = [0] * len(b)
dp = [i +1 for i in range(len(b))]
for i in range(len(b)):
    j = i+2
    check = 1
    while j <= len(b):
        if b[i:j] in a:
            check += 1
            j+=1
        else:
            break
    result[i] = check
# print(result)
# print(dp)

for i in range(len(b)):
    for j in range(result[i],0,-1):
        if j+i <len(b) and dp[i]+1 < dp[j+i]:
            dp[j+i] = dp[i]+1
# print(dp)
print(dp[len(b)-1])