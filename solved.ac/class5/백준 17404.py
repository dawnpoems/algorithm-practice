import sys
input = sys.stdin.readline

N = int(input())

costs = [[]]

for i in range(N) :
    costs.append(list(map(int, input().split())))


INF = 10 ** 9
ans = INF

for c in range(3) :
    dp = [[0] * 3 for _ in range(N + 1)]
    for i in range(3) :
        if c == i :
            dp[1][i] = costs[1][i]
        else :
            dp[1][i] = INF
    for i in range(2, N + 1) :
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
    for i in range(3) :
        if c != i :
            ans = min(ans, dp[-1][i])

print(ans)