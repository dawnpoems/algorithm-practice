import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 2

def get_cnt(num) :
    if dp[num] != 0 :
        return (dp[num])
    dp[num] = get_cnt(num - 1) + get_cnt(num - 2)
    return (dp[num])

print(get_cnt(n) % 10007)