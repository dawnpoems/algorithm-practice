import sys
input = sys.stdin.readline

N = int(input())
prices = list(map(int, input().split()))

dp = [0]
for i in range(N) :
    lst = []
    for j in range(i) :
        lst.append(dp[i - j] + prices[j])
    lst.append(prices[i])
    dp.append(max(lst))

print(dp[N])
