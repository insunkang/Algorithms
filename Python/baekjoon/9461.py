import sys

input = sys.stdin.readline

n = int(input())


result = []
for _ in range(n):
    dp = [0,1,1,1,2,2,3,4,5,7,9]
    s = int(input())
    if s < 10:
        result.append(dp[s])
        # print(dp[s])
    else:
        while len(dp) != s+1:
            dp.append(dp[len(dp)-1]+dp[len(dp)-5])
        result.append(dp[s])
        # print(dp[s])

for i in result:
    print(i)