import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 3

def get_tile(n) :
    if (dp[n] != 0) :
        return (dp[n])
    dp[n] = get_tile(n - 1) + (2 * get_tile(n - 2))
    return dp[n]

ans = get_tile(n)

print(ans % 10007)