import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []

dp = [0] * (K + 1)
dp[0] = 1

for i in range(N) :
    coin = int(input())
    coins.append(coin)
    
coins.sort()

# print(coins)
for c in coins :
    for k in range(1, K + 1) :
        if k - c >= 0 :
            dp[k] += dp[k - c]

print(dp[K])