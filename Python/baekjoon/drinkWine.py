n = int(input())
wine =  [0] * 10001

for i in range(1,n + 1):
    wine[i] = int(input())


dp = [0] * 10001


dp[1] = wine[1]
dp[2] = wine[1] + wine[2]
dp[3] = max(dp[2], dp[1]+wine[3],wine[2]+wine[3])
# dp[4] = max(dp[3],dp[2]+wine[4], dp[1]+wine[3]+wine[4])
if n > 3:
    for i in range(4, n + 1):
        dp[i] = max(dp[i-1],dp[i-2]+wine[i], dp[i-3]+wine[i]+wine[i-1])


print(dp[n])