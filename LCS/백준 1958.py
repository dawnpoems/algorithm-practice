import sys
input = sys.stdin.readline

one = list(input().strip())
two = list(input().strip())
three = list(input().strip())

N = len(one)
M = len(two)
K = len(three)

dp = [[[0] * (K + 1) for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1) :
    for j in range(1, M + 1) :
        for k in range(1, K + 1) :
            if one[i - 1] == two[j - 1] == three[k - 1] :
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
            else :
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

print(dp[N][M][K])