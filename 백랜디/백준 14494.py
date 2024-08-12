import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dp = [[0] * M for _ in range(N)]

dp[0][0] = 1

for i in range(N) :
    for j in range(M) :
        if i - 1 >= 0 :
            dp[i][j] += dp[i - 1][j]
        if j - 1 >= 0 :
            dp[i][j] += dp[i][j - 1]
        if i - 1 >= 0 and j - 1 >= 0 :
            dp[i][j] += dp[i - 1][j - 1]

# print(dp)
print(dp[N - 1][M - 1] % 1000000007)