import sys
input = sys.stdin.readline

n = int(input())

dp = [1e9] * 50001
dp[0] = 0
dp[1] = 1

for i in range(2, n + 1) :
    j = 1
    while j * j <= i :
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1

print(dp[n])