import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []

dp = [0] * (K + 1)

for i in range(N) :
    co = int(input())
    coins.append(co)
    dp[co] = 1
    now = co
    
coins.sort(reverse=True)

print(coins)
for i in range(1, K + 1) :
    nums = []
    for co in coins :
        if i - co >= 0 and i != co:
            nums.append(dp[i - co])
            dp[i] += dp[i - co]
    print(nums)

print(dp)