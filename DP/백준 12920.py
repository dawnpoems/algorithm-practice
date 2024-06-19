import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dp = [0] * (M + 1)

for i in range(N) :
    V, C, K = map(int, input().split())
    k = 1
    while K > 0 :
        num = min(k, K)
        for weight in range(M, V * num - 1, -1) :
            dp[weight] = max(dp[weight], dp[weight - V * num] + C * num)
        K -= num
        k *= 2

    # print(dp)
print(dp[-1])